import math

################## DATA ######################################

    # Tesis pura y dura ...

    # sept 2023,Roger Super Raceway	60.17m	Clockwise  (2022_september_pro_cw)
    # Optimal racing line (x, y, velocidad)
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

    def __init__(self, verbose=True):
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

        # sept 2023,Roger Super Raceway	60.17m	Clockwise  (2022_september_pro_cw)
        # Optimal racing line (x, y, velocidad)
        racing_track = [
            [4.82132, -3.63932, 3.84466, 0.06692],
            [4.6468, -3.82751, 3.86736, 0.06636],
            [4.46742, -4.01123, 3.89752, 0.06588],
            [4.28286, -4.1909, 3.94304, 0.06532],
            [4.09283, -4.3669, 4.0, 0.06475],
            [3.89708, -4.53959, 4.0, 0.06526],
            [3.69541, -4.70932, 4.0, 0.0659],
            [3.48765, -4.8764, 4.0, 0.06665],
            [3.27371, -5.04114, 4.0, 0.0675],
            [3.05353, -5.20381, 4.0, 0.06844],
            [2.82709, -5.36467, 4.0, 0.06944],
            [2.59448, -5.52394, 4.0, 0.07048],
            [2.35585, -5.68186, 4.0, 0.07154],
            [2.11145, -5.83861, 4.0, 0.07259],
            [1.86166, -5.99436, 3.54664, 0.083],
            [1.60697, -6.14925, 3.15512, 0.09448],
            [1.34825, -6.30322, 2.86645, 0.10503],
            [1.08901, -6.45472, 2.64228, 0.11364],
            [0.82904, -6.60079, 2.45909, 0.12126],
            [0.568, -6.73865, 2.30919, 0.12784],
            [0.30564, -6.86568, 2.17524, 0.13401],
            [0.0418, -6.97953, 2.05745, 0.13967],
            [-0.22361, -7.07803, 2.05745, 0.13759],
            [-0.49057, -7.15915, 2.05745, 0.13561],
            [-0.75899, -7.22096, 2.05745, 0.13388],
            [-1.02869, -7.26152, 2.05745, 0.13256],
            [-1.29939, -7.27862, 2.05745, 0.13183],
            [-1.57061, -7.26968, 2.21768, 0.12237],
            [-1.84178, -7.23811, 2.34411, 0.11646],
            [-2.1125, -7.18583, 2.49318, 0.11059],
            [-2.38249, -7.11469, 2.66824, 0.10464],
            [-2.65152, -7.02648, 2.88529, 0.09813],
            [-2.91948, -6.92312, 3.16036, 0.09087],
            [-3.1863, -6.80666, 3.53076, 0.08246],
            [-3.45203, -6.67936, 4.0, 0.07366],
            [-3.71683, -6.54364, 4.0, 0.07439],
            [-3.98093, -6.40207, 4.0, 0.07491],
            [-4.24469, -6.25732, 4.0, 0.07522],
            [-4.50851, -6.11209, 3.88356, 0.07754],
            [-4.77241, -5.96701, 2.78424, 0.10816],
            [-5.03644, -5.82216, 2.28175, 0.13198],
            [-5.30054, -5.67745, 1.97792, 0.15226],
            [-5.56466, -5.53276, 1.76789, 0.17034],
            [-5.82829, -5.38777, 1.6102, 0.18686],
            [-6.08328, -5.23752, 1.48677, 0.19906],
            [-6.32213, -5.07799, 1.38281, 0.20772],
            [-6.53864, -4.90648, 1.38281, 0.19974],
            [-6.72802, -4.72153, 1.38281, 0.19143],
            [-6.88651, -4.52258, 1.38281, 0.18395],
            [-7.01068, -4.30961, 1.38281, 0.17828],
            [-7.09652, -4.08287, 1.38281, 0.17533],
            [-7.13802, -3.84283, 1.53582, 0.15861],
            [-7.14163, -3.59361, 1.67981, 0.14838],
            [-7.11069, -3.33758, 1.86708, 0.13812],
            [-7.04866, -3.07664, 2.13375, 0.1257],
            [-6.9601, -2.81241, 1.82821, 0.15244],
            [-6.85097, -2.54618, 1.60828, 0.1789],
            [-6.72905, -2.27897, 1.45015, 0.20254],
            [-6.61417, -2.01506, 1.3, 0.2214],
            [-6.51705, -1.75475, 1.3, 0.21372],
            [-6.4463, -1.5, 1.3, 0.20338],
            [-6.40752, -1.25239, 1.3, 0.19279],
            [-6.40431, -1.01331, 1.3, 0.18392],
            [-6.43997, -0.7844, 1.3, 0.17821],
            [-6.52106, -0.56877, 1.42287, 0.16191],
            [-6.64066, -0.36575, 1.58647, 0.14853],
            [-6.79379, -0.17465, 1.82338, 0.1343],
            [-6.97527, 0.00573, 2.20836, 0.11587],
            [-7.17842, 0.1776, 2.21276, 0.12026],
            [-7.39436, 0.34433, 2.07487, 0.13149],
            [-7.61126, 0.52663, 1.95846, 0.14467],
            [-7.81508, 0.71709, 1.85206, 0.15062],
            [-8.00332, 0.91648, 1.85206, 0.14806],
            [-8.17369, 1.1253, 1.85206, 0.14551],
            [-8.32397, 1.34379, 1.85206, 0.14319],
            [-8.45188, 1.57205, 1.85206, 0.14128],
            [-8.55498, 1.80992, 1.85206, 0.13998],
            [-8.63031, 2.05707, 1.87737, 0.13763],
            [-8.6782, 2.31187, 1.90066, 0.13641],
            [-8.69851, 2.5729, 1.92224, 0.1362],
            [-8.69069, 2.83876, 1.94369, 0.13684],
            [-8.65383, 3.10796, 1.94422, 0.13975],
            [-8.58675, 3.37865, 1.79645, 0.15524],
            [-8.48821, 3.64836, 1.67701, 0.17123],
            [-8.35746, 3.91307, 1.5764, 0.18729],
            [-8.19895, 4.16199, 1.4849, 0.19873],
            [-8.02376, 4.38235, 1.4849, 0.18959],
            [-7.83492, 4.57295, 1.4849, 0.18069],
            [-7.63312, 4.73217, 1.4849, 0.17311],
            [-7.41906, 4.85852, 1.4849, 0.1674],
            [-7.1933, 4.94993, 1.4849, 0.16402],
            [-6.9563, 5.00274, 1.58037, 0.15365],
            [-6.71059, 5.02056, 1.69338, 0.14548],
            [-6.45804, 5.00585, 1.83205, 0.13809],
            [-6.20017, 4.96076, 2.00989, 0.13025],
            [-5.9384, 4.88771, 2.24898, 0.12084],
            [-5.67407, 4.78998, 2.59578, 0.10857],
            [-5.4084, 4.67203, 3.16511, 0.09184],
            [-5.14234, 4.53962, 4.0, 0.0743],
            [-4.87628, 4.39945, 4.0, 0.07518],
            [-4.61008, 4.25863, 4.0, 0.07529],
            [-4.34377, 4.11804, 4.0, 0.07529],
            [-4.0774, 3.97755, 4.0, 0.07529],
            [-3.81091, 3.83732, 4.0, 0.07528],
            [-3.5443, 3.69732, 4.0, 0.07528],
            [-3.27757, 3.55757, 4.0, 0.07528],
            [-3.01071, 3.41805, 4.0, 0.07528],
            [-2.74374, 3.27876, 4.0, 0.07528],
            [-2.47669, 3.13964, 4.0, 0.07528],
            [-2.20951, 3.00075, 4.0, 0.07528],
            [-1.94221, 2.86211, 4.0, 0.07528],
            [-1.67478, 2.72373, 3.57461, 0.08424],
            [-1.40721, 2.58562, 2.92532, 0.10293],
            [-1.13942, 2.44794, 2.53631, 0.11872],
            [-0.87121, 2.31109, 2.26893, 0.13271],
            [-0.60236, 2.17552, 2.06805, 0.1456],
            [-0.33315, 2.04576, 1.91056, 0.15642],
            [-0.06401, 1.92738, 1.77862, 0.16531],
            [0.20479, 1.82514, 1.66916, 0.17229],
            [0.4727, 1.74305, 1.54983, 0.1808],
            [0.73891, 1.6844, 1.54983, 0.17588],
            [1.0023, 1.65196, 1.54983, 0.17124],
            [1.26148, 1.64811, 1.54983, 0.16725],
            [1.51459, 1.67527, 1.54983, 0.16425],
            [1.75917, 1.73596, 1.54983, 0.16259],
            [1.99112, 1.83418, 1.61114, 0.15634],
            [2.20823, 1.96633, 1.67681, 0.15158],
            [2.40848, 2.12939, 1.75055, 0.14752],
            [2.59, 2.32047, 1.82946, 0.14406],
            [2.75108, 2.53668, 1.91996, 0.14043],
            [2.89043, 2.77485, 2.02315, 0.13639],
            [3.0073, 3.03156, 2.14426, 0.13154],
            [3.10167, 3.30323, 2.28833, 0.12568],
            [3.17436, 3.58626, 2.46554, 0.11852],
            [3.22698, 3.87728, 2.68813, 0.11002],
            [3.26186, 4.1733, 2.42783, 0.12277],
            [3.28181, 4.47189, 2.10892, 0.1419],
            [3.28997, 4.77137, 1.88574, 0.15887],
            [3.28956, 5.07085, 1.51844, 0.19723],
            [3.29662, 5.35399, 1.51844, 0.18652],
            [3.31667, 5.62824, 1.51844, 0.1811],
            [3.35441, 5.89244, 1.51844, 0.17576],
            [3.41383, 6.14551, 1.51844, 0.1712],
            [3.49862, 6.38583, 1.51844, 0.16783],
            [3.61984, 6.60576, 1.56847, 0.16011],
            [3.77256, 6.80393, 1.62194, 0.15426],
            [3.95254, 6.97893, 1.67626, 0.14976],
            [4.15612, 7.12949, 1.73398, 0.14603],
            [4.37998, 7.25463, 1.79727, 0.14269],
            [4.62104, 7.35364, 1.8663, 0.13964],
            [4.87643, 7.42611, 1.9423, 0.13668],
            [5.14344, 7.47193, 2.02512, 0.13377],
            [5.41947, 7.49124, 2.11794, 0.13065],
            [5.70204, 7.48457, 2.2218, 0.12721],
            [5.98869, 7.45282, 2.33669, 0.12342],
            [6.27701, 7.39731, 2.23512, 0.13136],
            [6.56457, 7.31995, 2.05545, 0.14488],
            [6.84889, 7.2231, 1.91224, 0.15708],
            [7.12781, 7.10968, 1.79256, 0.16797],
            [7.39768, 6.98145, 1.68773, 0.17704],
            [7.65166, 6.83736, 1.55916, 0.18728],
            [7.88486, 6.67702, 1.55916, 0.18151],
            [8.09394, 6.50052, 1.55916, 0.17549],
            [8.27637, 6.30831, 1.55916, 0.16997],
            [8.42987, 6.10099, 1.55916, 0.16545],
            [8.55182, 5.87921, 1.55916, 0.16233],
            [8.63723, 5.64325, 1.65833, 0.15132],
            [8.68981, 5.39674, 1.77291, 0.14217],
            [8.71254, 5.14222, 1.91334, 0.13355],
            [8.70821, 4.88162, 2.09053, 0.12467],
            [8.67971, 4.61644, 2.32564, 0.11468],
            [8.63032, 4.34779, 2.66128, 0.10264],
            [8.56384, 4.07649, 3.19703, 0.08737],
            [8.48475, 3.80313, 4.0, 0.07114],
            [8.39827, 3.52845, 4.0, 0.07199],
            [8.30771, 3.24718, 4.0, 0.07387],
            [8.21534, 2.96689, 4.0, 0.07378],
            [8.12099, 2.68739, 4.0, 0.07375],
            [8.02452, 2.40866, 4.0, 0.07374],
            [7.92582, 2.13071, 4.0, 0.07374],
            [7.82476, 1.85356, 4.0, 0.07375],
            [7.72123, 1.57722, 4.0, 0.07377],
            [7.6151, 1.30172, 4.0, 0.07381],
            [7.50625, 1.02708, 4.0, 0.07386],
            [7.39457, 0.75333, 4.0, 0.07391],
            [7.27992, 0.4805, 4.0, 0.07398],
            [7.16215, 0.20863, 4.0, 0.07407],
            [7.04109, -0.06223, 4.0, 0.07417],
            [6.91656, -0.33203, 4.0, 0.07429],
            [6.78836, -0.60072, 4.0, 0.07443],
            [6.65628, -0.86823, 4.0, 0.07458],
            [6.51992, -1.13441, 4.0, 0.07477],
            [6.37895, -1.39865, 4.0, 0.07487],
            [6.23406, -1.65862, 4.0, 0.0744],
            [6.08671, -1.91102, 3.94159, 0.07415],
            [5.93757, -2.15437, 3.89484, 0.07328],
            [5.7866, -2.38865, 3.87664, 0.07189],
            [5.63348, -2.61444, 3.84466, 0.07096],
            [5.4778, -2.83242, 3.84466, 0.06967],
            [5.31915, -3.0433, 3.84466, 0.06864],
            [5.15711, -3.2477, 3.84466, 0.06784],
            [4.99129, -3.44619, 3.84466, 0.06727]
        ]

        #################### RACING LINE - END ######################





        # Get closest indexes for racing line (and distances to all points on racing line)
        closest_index, second_closest_index = closest_2_racing_points_index(
            racing_track, [x, y])

        # Get optimal [x, y, speed, time] for closest and second closest index
        optimals        = racing_track[closest_index]
        optimals_second = racing_track[second_closest_index]

        # Save first racingpoint of episode for later
        if self.verbose == True:
            self.first_racingpoint_index = 0 # this is just for testing purposes
        if steps == 1:
            self.first_racingpoint_index = closest_index




        ################ REWARD AND PUNISHMENT ################
        #
        # 0.001   	1m (mili)	10^-3   1e-3 
        # 1,000	    1k (kilo)	10^3	1e3
        #

        ZERO_VALUE = 1e-3


        ## Define the default reward ##
        reward = 1

        ## Reward if car goes close to optimal racing line ##
        DISTANCE_MULTIPLE = 1
        dist = dist_to_racing_line(optimals[0:2], optimals_second[0:2], [x, y])
        distance_reward = max(ZERO_VALUE, 1 - (dist/(track_width*0.5)))
        reward += distance_reward * DISTANCE_MULTIPLE


        ## Zero reward if off track ##
        if all_wheels_on_track == False:
            reward = ZERO_VALUE
            
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
    
    
    
