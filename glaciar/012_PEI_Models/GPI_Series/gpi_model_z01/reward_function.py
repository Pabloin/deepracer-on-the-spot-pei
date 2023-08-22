import math


################## HELPER STATIC FUNCTIONS ###################


#----------------------------------------------------------------------------------------------------
# Calculate distances between two points
def dist_2_points(x1, x2, y1, y2):
    return abs(abs(x1-x2)**2 + abs(y1-y2)**2)**0.5



#----------------------------------------------------------------------------------------------------
# closest 2 racing points index
def closest_2_racing_points_index(racing_coords, car_coords):

    # Calculate all distances to racing points
    distances = []
    for i in range(len(racing_coords)):
        distance = dist_2_points(x1=racing_coords[i][0], x2=car_coords[0],
                                        y1=racing_coords[i][1], y2=car_coords[1])
        distances.append(distance)

    # Get index of the closest racing point
    closest_index = distances.index(min(distances))

    # Get index of the second closest racing point
    distances_no_closest = distances.copy()
    distances_no_closest[closest_index] = 999
    second_closest_index = distances_no_closest.index(min(distances_no_closest))

    return [closest_index, second_closest_index]



#----------------------------------------------------------------------------------------------------
# Distance to racing line
def dist_to_racing_line(closest_coords, second_closest_coords, car_coords):
    
    # Calculate the distances between 2 closest racing points
    a = abs(dist_2_points(x1=closest_coords[0],
                            x2=second_closest_coords[0],
                            y1=closest_coords[1],
                            y2=second_closest_coords[1]))

    # Distances between car and closest and second closest racing point
    b = abs(dist_2_points(x1=car_coords[0],
                            x2=closest_coords[0],
                            y1=car_coords[1],
                            y2=closest_coords[1]))
    c = abs(dist_2_points(x1=car_coords[0],
                            x2=second_closest_coords[0],
                            y1=car_coords[1],
                            y2=second_closest_coords[1]))

    # Calculate distance between car and racing line
    # (goes through 2 closest racing points)
    # try-except in case a=0 (rare bug in DeepRacer)
    try:
        distance = abs(-(a**4) + 2*(a**2)*(b**2) + 2*(a**2)*(c**2) -
                        (b**4) + 2*(b**2)*(c**2) - (c**4))**0.5 / (2*a)
    except:
        distance = b

    return distance



#----------------------------------------------------------------------------------------------------
# Calculate which one of the closest racing points is the next one and which one the previous one
def next_prev_racing_point(closest_coords, second_closest_coords, car_coords, heading):

    # Virtually set the car more into the heading direction
    heading_vector = [math.cos(math.radians(
        heading)), math.sin(math.radians(heading))]
    new_car_coords = [car_coords[0]+heading_vector[0],
                        car_coords[1]+heading_vector[1]]

    # Calculate distance from new car coords to 2 closest racing points
    distance_closest_coords_new = dist_2_points(x1=new_car_coords[0],
                                                x2=closest_coords[0],
                                                y1=new_car_coords[1],
                                                y2=closest_coords[1])
    distance_second_closest_coords_new = dist_2_points(x1=new_car_coords[0],
                                                        x2=second_closest_coords[0],
                                                        y1=new_car_coords[1],
                                                        y2=second_closest_coords[1])

    if distance_closest_coords_new <= distance_second_closest_coords_new:
        next_point_coords = closest_coords
        prev_point_coords = second_closest_coords
    else:
        next_point_coords = second_closest_coords
        prev_point_coords = closest_coords

    return [next_point_coords, prev_point_coords]




#----------------------------------------------------------------------------------------------------
# Racing direction diff
def racing_direction_diff(closest_coords, second_closest_coords, car_coords, heading):

    # Calculate the direction of the center line based on the closest waypoints
    next_point, prev_point = next_prev_racing_point(closest_coords,
                                                    second_closest_coords,
                                                    car_coords,
                                                    heading)

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(
        next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    return direction_diff



#----------------------------------------------------------------------------------------------------
# Gives back indexes that lie between start and end index of a cyclical list 
# (start index is included, end index is not)
def indexes_cyclical(start, end, array_len):

    if end < start:
        end += array_len

    return [index % array_len for index in range(start, end)]



#----------------------------------------------------------------------------------------------------
# Calculate how long car would take for entire lap, if it continued like it did until now
def projected_time(first_index, closest_index, step_count, times_list):

    # Calculate how much time has passed since start
    current_actual_time = (step_count-1) / 15

    # Calculate which indexes were already passed
    indexes_traveled = indexes_cyclical(first_index, closest_index, len(times_list))

    # Calculate how much time should have passed if car would have followed optimals
    current_expected_time = sum([times_list[i] for i in indexes_traveled])

    # Calculate how long one entire lap takes if car follows optimals
    total_expected_time = sum(times_list)

    # Calculate how long car would take for entire lap, if it continued like it did until now
    try:
        projected_time = (current_actual_time/current_expected_time) * total_expected_time
    except:
        projected_time = 9999

    return projected_time
    

################## HELPER STATIC FUNCTIONS - END ###################



class MyRewardClassZ01:

    def __init__(self, verbose=False):
        self.first_racingpoint_index = None
        self.verbose = verbose


    def reward_function_z01(self, params):

       
        ################## INPUT PARAMETERS ###################

        # Read all input parameters
        x = params['x']
        y = params['y']

        steps    = params['steps']
        speed    = params['speed']
        heading  = params['heading']
        progress = params['progress']

        is_left_of_center    = params['is_left_of_center']
        distance_from_center = params['distance_from_center']
        all_wheels_on_track  = params['all_wheels_on_track']
        is_offtrack          = params['is_offtrack']

        steering_angle       = params['steering_angle']
        track_width          = params['track_width']
        waypoints            = params['waypoints']
        closest_waypoints    = params['closest_waypoints']

        ############### OPTIMAL X,Y,SPEED,TIME ################



        #################### RACING LINE ######################

        # Rogue Raceway  aka  2022_march_pro
        # Optimal racing line, debería ser:
        # Each row: [x,y,speed,timeFromPreviousPoint]
        racing_track = [
            [ 6.32350560e-01, -3.88212448e-01, 0, 0 ],
            [ 8.95432720e-01, -4.68818002e-01, 0, 0 ],
            [ 1.15943611e+00, -5.42195235e-01, 0, 0 ],
            [ 1.42436073e+00, -6.08344148e-01, 0, 0 ],
            [ 1.69020658e+00, -6.67264741e-01, 0, 0 ],
            [ 1.95697366e+00, -7.18957013e-01, 0, 0 ],
            [ 2.22466197e+00, -7.63420965e-01, 0, 0 ],
            [ 2.49327151e+00, -8.00656596e-01, 0, 0 ],
            [ 2.76280228e+00, -8.30663907e-01, 0, 0 ],
            [ 3.03325428e+00, -8.53442897e-01, 0, 0 ],
            [ 3.30462751e+00, -8.68993567e-01, 0, 0 ],
            [ 3.57692197e+00, -8.77315916e-01, 0, 0 ],
            [ 3.85013767e+00, -8.78409945e-01, 0, 0 ],
            [ 4.12427459e+00, -8.72275654e-01, 0, 0 ],
            [ 4.39933274e+00, -8.58913042e-01, 0, 0 ],
            [ 4.67531212e+00, -8.38322109e-01, 0, 0 ],
            [ 4.95101825e+00, -8.08611414e-01, 0, 0 ],
            [ 5.21825688e+00, -7.56805507e-01, 0, 0 ],
            [ 5.47547547e+00, -6.80445937e-01, 0, 0 ],
            [ 5.72267399e+00, -5.79532704e-01, 0, 0 ],
            [ 5.95985247e+00, -4.54065808e-01, 0, 0 ],
            [ 6.18701089e+00, -3.04045250e-01, 0, 0 ],
            [ 6.40414926e+00, -1.29471028e-01, 0, 0 ],
            [ 6.61104421e+00,  6.93744769e-02, 0, 0 ],
            [ 6.79978109e+00,  2.82485196e-01, 0, 0 ],
            [ 6.96642063e+00,  5.04880938e-01, 0, 0 ],
            [ 7.11096283e+00,  7.36561704e-01, 0, 0 ],
            [ 7.23340768e+00,  9.77527494e-01, 0, 0 ],
            [ 7.33375520e+00,  1.22777831e+00, 0, 0 ],
            [ 7.41200537e+00,  1.48731414e+00, 0, 0 ],
            [ 7.46815821e+00,  1.75613500e+00, 0, 0 ],
            [ 7.50221370e+00,  2.03424089e+00, 0, 0 ],
            [ 7.51422913e+00,  2.32144713e+00, 0, 0 ],
            [ 7.50722825e+00,  2.60800699e+00, 0, 0 ],
            [ 7.48292433e+00,  2.88839783e+00, 0, 0 ],
            [ 7.44131737e+00,  3.16261965e+00, 0, 0 ],
            [ 7.38240737e+00,  3.43067245e+00, 0, 0 ],
            [ 7.30619433e+00,  3.69255623e+00, 0, 0 ],
            [ 7.21267826e+00,  3.94827099e+00, 0, 0 ],
            [ 7.10185915e+00,  4.19781674e+00, 0, 0 ],
            [ 6.97373700e+00,  4.44119346e+00, 0, 0 ],
            [ 6.82831181e+00,  4.67840116e+00, 0, 0 ],
            [ 6.66558359e+00,  4.90943985e+00, 0, 0 ],
            [ 6.48560186e+00,  5.13406868e+00, 0, 0 ],
            [ 6.29027536e+00,  5.34300755e+00, 0, 0 ],
            [ 6.08058266e+00,  5.53149877e+00, 0, 0 ],
            [ 5.85652375e+00,  5.69954236e+00, 0, 0 ],
            [ 5.61809862e+00,  5.84713830e+00, 0, 0 ],
            [ 5.36530729e+00,  5.97428661e+00, 0, 0 ],
            [ 5.09814976e+00,  6.08098727e+00, 0, 0 ],
            [ 4.81662601e+00,  6.16724029e+00, 0, 0 ],
            [ 4.52073605e+00,  6.23304568e+00, 0, 0 ],
            [ 4.21047989e+00,  6.27840342e+00, 0, 0 ],
            [ 3.88585751e+00,  6.30331353e+00, 0, 0 ],
            [ 3.54686893e+00,  6.30777599e+00, 0, 0 ],
            [ 3.19846287e+00,  6.29043966e+00, 0, 0 ],
            [ 2.88442936e+00,  6.23934847e+00, 0, 0 ],
            [ 2.61506149e+00,  6.15169209e+00, 0, 0 ],
            [ 2.39035926e+00,  6.02747052e+00, 0, 0 ],
            [ 2.21032267e+00,  5.86668376e+00, 0, 0 ],
            [ 2.07495170e+00,  5.66933182e+00, 0, 0 ],
            [ 1.98424638e+00,  5.43541469e+00, 0, 0 ],
            [ 1.93820669e+00,  5.16493236e+00, 0, 0 ],
            [ 1.93684166e+00,  4.85795071e+00, 0, 0 ],
            [ 1.98651122e+00,  4.56088667e+00, 0, 0 ],
            [ 2.09267819e+00,  4.31360986e+00, 0, 0 ],
            [ 2.25534258e+00,  4.11612030e+00, 0, 0 ],
            [ 2.47450440e+00,  3.96841798e+00, 0, 0 ],
            [ 2.75016363e+00,  3.87050291e+00, 0, 0 ],
            [ 3.08232027e+00,  3.82237507e+00, 0, 0 ],
            [ 3.41744145e+00,  3.78295625e+00, 0, 0 ],
            [ 3.68073018e+00,  3.69485137e+00, 0, 0 ],
            [ 3.87168328e+00,  3.55767429e+00, 0, 0 ],
            [ 3.99030073e+00,  3.37142500e+00, 0, 0 ],
            [ 4.03658253e+00,  3.13610351e+00, 0, 0 ],
            [ 4.01052870e+00,  2.85170981e+00, 0, 0 ],
            [ 3.91708985e+00,  2.52977821e+00, 0, 0 ],
            [ 3.78945598e+00,  2.24763690e+00, 0, 0 ],
            [ 3.63378358e+00,  2.01962962e+00, 0, 0 ],
            [ 3.45007263e+00,  1.84575637e+00, 0, 0 ],
            [ 3.23832314e+00,  1.72601715e+00, 0, 0 ],
            [ 2.99853511e+00,  1.66041196e+00, 0, 0 ],
            [ 2.73070854e+00,  1.64894080e+00, 0, 0 ],
            [ 2.43484342e+00,  1.69160367e+00, 0, 0 ],
            [ 2.12567806e+00,  1.76017346e+00, 0, 0 ],
            [ 1.82284106e+00,  1.81705703e+00, 0, 0 ],
            [ 1.52642986e+00,  1.86206780e+00, 0, 0 ],
            [ 1.23644445e+00,  1.89520576e+00, 0, 0 ],
            [ 9.52884822e-01,  1.91647092e+00, 0, 0 ],
            [ 6.75750986e-01,  1.92586327e+00, 0, 0 ],
            [ 4.05042940e-01,  1.92338282e+00, 0, 0 ],
            [ 1.40760683e-01,  1.90902957e+00, 0, 0 ],
            [-1.21395629e-01,  1.88647803e+00, 0, 0 ],
            [-3.89980426e-01,  1.86303855e+00, 0, 0 ],
            [-6.65228573e-01,  1.83891186e+00, 0, 0 ],
            [-9.47140070e-01,  1.81409794e+00, 0, 0 ],
            [-1.20485814e+00,  1.83475076e+00, 0, 0 ],
            [-1.37425587e+00,  1.99678799e+00, 0, 0 ],
            [-1.45502337e+00,  2.29689403e+00, 0, 0 ],
            [-1.47864237e+00,  2.61686061e+00, 0, 0 ],
            [-1.45704828e+00,  2.91187246e+00, 0, 0 ],
            [-1.39024109e+00,  3.18192957e+00, 0, 0 ],
            [-1.27887839e+00,  3.42735566e+00, 0, 0 ],
            [-1.17162496e+00,  3.67210649e+00, 0, 0 ],
            [-1.09866651e+00,  3.93104132e+00, 0, 0 ],
            [-1.06000304e+00,  4.20416014e+00, 0, 0 ],
            [-1.05563457e+00,  4.49146296e+00, 0, 0 ],
            [-1.08556108e+00,  4.79294977e+00, 0, 0 ],
            [-1.14978258e+00,  5.10862058e+00, 0, 0 ],
            [-1.24829907e+00,  5.43847539e+00, 0, 0 ],
            [-1.37414027e+00,  5.76275095e+00, 0, 0 ],
            [-1.51126800e+00,  6.03597305e+00, 0, 0 ],
            [-1.65904492e+00,  6.25633470e+00, 0, 0 ],
            [-1.81747104e+00,  6.42383589e+00, 0, 0 ],
            [-1.98654637e+00,  6.53847662e+00, 0, 0 ],
            [-2.16627089e+00,  6.60025690e+00, 0, 0 ],
            [-2.35664462e+00,  6.60917672e+00, 0, 0 ],
            [-2.55766754e+00,  6.56523608e+00, 0, 0 ],
            [-2.76933967e+00,  6.46843498e+00, 0, 0 ],
            [-2.99166100e+00,  6.31877342e+00, 0, 0 ],
            [-3.22463153e+00,  6.11625141e+00, 0, 0 ],
            [-3.46704631e+00,  5.86453552e+00, 0, 0 ],
            [-3.70433269e+00,  5.60796927e+00, 0, 0 ],
            [-3.93220875e+00,  5.35958220e+00, 0, 0 ],
            [-4.15067451e+00,  5.11937430e+00, 0, 0 ],
            [-4.35972996e+00,  4.88734556e+00, 0, 0 ],
            [-4.55937510e+00,  4.66349600e+00, 0, 0 ],
            [-4.74960993e+00,  4.44782560e+00, 0, 0 ],
            [-4.93043445e+00,  4.24033437e+00, 0, 0 ],
            [-5.10397432e+00,  4.03637659e+00, 0, 0 ],
            [-5.27362953e+00,  3.82852139e+00, 0, 0 ],
            [-5.43944457e+00,  3.61667156e+00, 0, 0 ],
            [-5.60141941e+00,  3.40082712e+00, 0, 0 ],
            [-5.75955408e+00,  3.18098805e+00, 0, 0 ],
            [-5.91384857e+00,  2.95715436e+00, 0, 0 ],
            [-6.06430287e+00,  2.72932605e+00, 0, 0 ],
            [-6.21091700e+00,  2.49750312e+00, 0, 0 ],
            [-6.35365721e+00,  2.26168324e+00, 0, 0 ],
            [-6.48891910e+00,  2.02161787e+00, 0, 0 ],
            [-6.61427625e+00,  1.77713969e+00, 0, 0 ],
            [-6.72972865e+00,  1.52824872e+00, 0, 0 ],
            [-6.83527632e+00,  1.27494493e+00, 0, 0 ],
            [-6.93091924e+00,  1.01722835e+00, 0, 0 ],
            [-7.01665742e+00,  7.55098956e-01, 0, 0 ],
            [-7.09249087e+00,  4.88556761e-01, 0, 0 ],
            [-7.15841957e+00,  2.17601763e-01, 0, 0 ],
            [-7.21444353e+00, -5.77660399e-02, 0, 0 ],
            [-7.26056274e+00, -3.37546647e-01, 0, 0 ],
            [-7.29677722e+00, -6.21740057e-01, 0, 0 ],
            [-7.32308696e+00, -9.10346272e-01, 0, 0 ],
            [-7.33949195e+00, -1.20336529e+00, 0, 0 ],
            [-7.34599221e+00, -1.50079711e+00, 0, 0 ],
            [-7.34258772e+00, -1.80264174e+00, 0, 0 ],
            [-7.32927849e+00, -2.10889917e+00, 0, 0 ],
            [-7.30602438e+00, -2.41944782e+00, 0, 0 ],
            [-7.26907459e+00, -2.72292786e+00, 0, 0 ],
            [-7.21597420e+00, -3.01190417e+00, 0, 0 ],
            [-7.14672320e+00, -3.28637674e+00, 0, 0 ],
            [-7.06132160e+00, -3.54634558e+00, 0, 0 ],
            [-6.95976939e+00, -3.79181068e+00, 0, 0 ],
            [-6.84206658e+00, -4.02277205e+00, 0, 0 ],
            [-6.70821316e+00, -4.23922968e+00, 0, 0 ],
            [-6.55820913e+00, -4.44118358e+00, 0, 0 ],
            [-6.39205450e+00, -4.62863375e+00, 0, 0 ],
            [-6.20974927e+00, -4.80158018e+00, 0, 0 ],
            [-6.01129343e+00, -4.96002287e+00, 0, 0 ],
            [-5.79668698e+00, -5.10396183e+00, 0, 0 ],
            [-5.56592993e+00, -5.23339706e+00, 0, 0 ],
            [-5.31902228e+00, -5.34832855e+00, 0, 0 ],
            [-5.05624476e+00, -5.44896183e+00, 0, 0 ],
            [-4.78734294e+00, -5.54243118e+00, 0, 0 ],
            [-4.51713121e+00, -5.63226104e+00, 0, 0 ],
            [-4.24560959e+00, -5.71845139e+00, 0, 0 ],
            [-3.97277807e+00, -5.80100223e+00, 0, 0 ],
            [-3.69863665e+00, -5.87991357e+00, 0, 0 ],
            [-3.42318533e+00, -5.95518541e+00, 0, 0 ],
            [-3.14642411e+00, -6.02681775e+00, 0, 0 ],
            [-2.86835300e+00, -6.09481058e+00, 0, 0 ],
            [-2.58897198e+00, -6.15916391e+00, 0, 0 ],
            [-2.30828106e+00, -6.21987774e+00, 0, 0 ],
            [-2.02628025e+00, -6.27695206e+00, 0, 0 ],
            [-1.74296954e+00, -6.33038688e+00, 0, 0 ],
            [-1.45834893e+00, -6.38018219e+00, 0, 0 ],
            [-1.17241842e+00, -6.42633801e+00, 0, 0 ],
            [-8.85178008e-01, -6.46885432e+00, 0, 0 ],
            [-5.96627700e-01, -6.50773112e+00, 0, 0 ],
            [-3.06767493e-01, -6.54296843e+00, 0, 0 ],
            [-1.56770178e-02, -6.57441653e+00, 0, 0 ],
            [ 2.72497782e-01, -6.59428162e+00, 0, 0 ],
            [ 5.55417167e-01, -6.59816530e+00, 0, 0 ],
            [ 8.33081137e-01, -6.58606757e+00, 0, 0 ],
            [ 1.10548969e+00, -6.55798843e+00, 0, 0 ],
            [ 1.37264283e+00, -6.51392788e+00, 0, 0 ],
            [ 1.63454056e+00, -6.45388592e+00, 0, 0 ],
            [ 1.89118287e+00, -6.37786254e+00, 0, 0 ],
            [ 2.14256976e+00, -6.28585776e+00, 0, 0 ],
            [ 2.38870124e+00, -6.17787157e+00, 0, 0 ],
            [ 2.62957731e+00, -6.05390397e+00, 0, 0 ],
            [ 2.86519796e+00, -5.91395495e+00, 0, 0 ],
            [ 3.09556319e+00, -5.75802453e+00, 0, 0 ],
            [ 3.32067301e+00, -5.58611269e+00, 0, 0 ],
            [ 3.54052742e+00, -5.39821945e+00, 0, 0 ],
            [ 3.75512641e+00, -5.19434479e+00, 0, 0 ],
            [ 3.93986477e+00, -4.97567950e+00, 0, 0 ],
            [ 4.05918358e+00, -4.74394445e+00, 0, 0 ],
            [ 4.11279393e+00, -4.49915363e+00, 0, 0 ],
            [ 4.10069583e+00, -4.24130703e+00, 0, 0 ],
            [ 4.02288926e+00, -3.97040466e+00, 0, 0 ],
            [ 3.87965504e+00, -3.68692812e+00, 0, 0 ],
            [ 3.69633545e+00, -3.43434087e+00, 0, 0 ],
            [ 3.48939191e+00, -3.24087518e+00, 0, 0 ],
            [ 3.25882442e+00, -3.10653108e+00, 0, 0 ],
            [ 3.00463298e+00, -3.03130854e+00, 0, 0 ],
            [ 2.72900322e+00, -3.01041817e+00, 0, 0 ],
            [ 2.45149296e+00, -3.00100243e+00, 0, 0 ],
            [ 2.17673970e+00, -2.99289908e+00, 0, 0 ],
            [ 1.90474344e+00, -2.98610812e+00, 0, 0 ],
            [ 1.63550418e+00, -2.98062954e+00, 0, 0 ],
            [ 1.36902192e+00, -2.97646334e+00, 0, 0 ],
            [ 1.10295617e+00, -2.97506274e+00, 0, 0 ],
            [ 8.32997953e-01, -2.97910320e+00, 0, 0 ],
            [ 5.59053411e-01, -2.98864298e+00, 0, 0 ],
            [ 2.81122548e-01, -3.00368208e+00, 0, 0 ],
            [-7.94636103e-04, -3.02422051e+00, 0, 0 ],
            [-2.86698142e-01, -3.05025826e+00, 0, 0 ],
            [-5.76587968e-01, -3.08179533e+00, 0, 0 ],
            [-8.70464116e-01, -3.11883173e+00, 0, 0 ],
            [-1.16832659e+00, -3.16136745e+00, 0, 0 ],
            [-1.47017538e+00, -3.20940250e+00, 0, 0 ],
            [-1.77601049e+00, -3.26293687e+00, 0, 0 ],
            [-2.08553612e+00, -3.32142581e+00, 0, 0 ],
            [-2.38547228e+00, -3.36041224e+00, 0, 0 ],
            [-2.66865682e+00, -3.36670605e+00, 0, 0 ],
            [-2.93508974e+00, -3.34030723e+00, 0, 0 ],
            [-3.18477105e+00, -3.28121579e+00, 0, 0 ],
            [-3.41770075e+00, -3.18943172e+00, 0, 0 ],
            [-3.63387883e+00, -3.06495503e+00, 0, 0 ],
            [-3.83330529e+00, -2.90778571e+00, 0, 0 ],
            [-4.01598014e+00, -2.71792376e+00, 0, 0 ],
            [-4.18190337e+00, -2.49536919e+00, 0, 0 ],
            [-4.33107499e+00, -2.24012199e+00, 0, 0 ],
            [-4.46349499e+00, -1.95218217e+00, 0, 0 ],
            [-4.57916338e+00, -1.63154972e+00, 0, 0 ],
            [-4.66644298e+00, -1.30628012e+00, 0, 0 ],
            [-4.70803751e+00, -1.01807209e+00, 0, 0 ],
            [-4.70378470e+00, -7.67316846e-01, 0, 0 ],
            [-4.65368456e+00, -5.54014394e-01, 0, 0 ],
            [-4.55773707e+00, -3.78164734e-01, 0, 0 ],
            [-4.41594224e+00, -2.39767864e-01, 0, 0 ],
            [-4.22830007e+00, -1.38823786e-01, 0, 0 ],
            [-3.99481056e+00, -7.53324991e-02, 0, 0 ],
            [-3.71547370e+00, -4.92940032e-02, 0, 0 ],
            [-3.39065704e+00, -6.04481205e-02, 0, 0 ],
            [-3.05365598e+00, -8.52248442e-02, 0, 0 ],
            [-2.72611622e+00, -1.08301068e-01, 0, 0 ],
            [-2.40803775e+00, -1.29676791e-01, 0, 0 ],
            [-2.09942058e+00, -1.49352014e-01, 0, 0 ],
            [-1.80026471e+00, -1.67326737e-01, 0, 0 ],
            [-1.51057013e+00, -1.83600960e-01, 0, 0 ],
            [-1.23033684e+00, -1.98174682e-01, 0, 0 ],
            [-9.59564856e-01, -2.11047905e-01, 0, 0 ],
            [-6.96752105e-01, -2.23448150e-01, 0, 0 ],
            [-4.33752088e-01, -2.42032960e-01, 0, 0 ],
            [-1.69341813e-01, -2.67801794e-01, 0, 0 ],
            [ 9.64787202e-02, -3.00754653e-01, 0, 0 ],
            [ 3.63709511e-01, -3.40891538e-01, 0, 0 ],
            [ 6.32350560e-01, -3.88212448e-01, 0, 0 ]
        ]


        #################### RACING LINE - END ######################





        # Get closest indexes for racing line (and distances to all points on racing line)
        closest_index, second_closest_index = closest_2_racing_points_index(
            racing_track, [x, y])

        # Get optimal [x, y, speed, time] for closest and second closest index
        optimals = racing_track[closest_index]
        optimals_second = racing_track[second_closest_index]

        # Save first racingpoint of episode for later
        if self.verbose == True:
            self.first_racingpoint_index = 0 # this is just for testing purposes
        if steps == 1:
            self.first_racingpoint_index = closest_index




        ################ REWARD AND PUNISHMENT ################
  
        ## Define the default reward ##
        reward = 1

        ## Reward if car goes close to optimal racing line ##
        DISTANCE_MULTIPLE = 1
        dist = dist_to_racing_line(optimals[0:2], optimals_second[0:2], [x, y])
        distance_reward = max(1e-3, 1 - (dist/(track_width*0.5)))
        reward += distance_reward * DISTANCE_MULTIPLE


        ## Zero reward if off track ##
        if all_wheels_on_track == False:
            reward = 1e-3
            
        ####################### VERBOSE #######################
        
        if self.verbose == True:
            print("Closest index: %i" % closest_index)
            print("Distance to racing line: %f" % dist)
            print("=== Distance reward (w/out multiple): %f ===" % (distance_reward))
            print("Optimal speed: %f" % optimals[2])
            # print("Speed difference: %f" % speed_diff)
            # print("=== Speed reward(w/out multiple): %f ===" % speed_reward)
            # print("Direction difference: %f" % direction_diff)
            print("Predicted time: %f" % projected_time)
            # print("=== Steps reward: %f ===" % steps_reward)
            # print("=== Finish reward: %f ===" % finish_reward)
            
        #################### RETURN REWARD ####################
        return float(reward)



myRewardObject = MyRewardClassZ01() 

def reward_function(params):
    return myRewardObject.reward_function_z01(params)
    
    
    
