import math

################## DATA ######################################

    # Rogue Raceway  aka  2022_march_pro
    #                     (76.76m) 

    # PRO - 
    #    OBJ CW -- Clockwise 
    #       Time TBS
    #       vuelta 1 - TBD   (0 off)
    #       vuelta 2 - TBD   (? off   zona 3) 

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


    def reward_function_z01(self, True, params):

       
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
        # Each row: [x,y,speed,timeFromPreviousPoint,  waypoint]
        racing_track = [
            [0.89414, -0.39536, 4.0, 0.06262],
            [0.64688, -0.37173, 4.0, 0.0621],
            [0.40178, -0.34807, 4.0, 0.06156],
            [0.15899, -0.3244, 4.0, 0.06099],
            [-0.08085, -0.30068, 4.0, 0.06025],
            [-0.33696, -0.27614, 4.0, 0.06432],
            [-0.60425, -0.2521, 4.0, 0.06709],
            [-0.88142, -0.22976, 4.0, 0.06952],
            [-1.16535, -0.21055, 3.77642, 0.07536],
            [-1.4528, -0.19593, 3.38335, 0.08507],
            [-1.74099, -0.18734, 3.00667, 0.09589],
            [-2.02764, -0.18634, 2.71977, 0.1054],
            [-2.31085, -0.19447, 2.37626, 0.11923],
            [-2.58891, -0.21327, 2.09323, 0.13314],
            [-2.85995, -0.24465, 1.82489, 0.14951],
            [-3.12188, -0.29051, 1.82489, 0.14572],
            [-3.37213, -0.35305, 1.6954, 0.15214],
            [-3.6081, -0.43375, 1.4966, 0.16664],
            [-3.82552, -0.53519, 1.4966, 0.16031],
            [-4.01928, -0.65912, 1.41418, 0.16264],
            [-4.18215, -0.8066, 1.41418, 0.15537],
            [-4.31712, -0.97099, 1.41418, 0.1504],
            [-4.41757, -1.15182, 1.41418, 0.14627],
            [-4.47379, -1.34671, 1.41418, 0.14343],
            [-4.48841, -1.54838, 1.41418, 0.14298],
            [-4.45179, -1.75013, 1.53855, 0.13327],
            [-4.37043, -1.94434, 1.70123, 0.12377],
            [-4.25094, -2.12681, 1.8563, 0.1175],
            [-4.09777, -2.29474, 2.02148, 0.11244],
            [-3.9147, -2.44609, 2.20886, 0.10754],
            [-3.70544, -2.57959, 2.42698, 0.10228],
            [-3.47382, -2.69482, 2.68113, 0.09649],
            [-3.22375, -2.79212, 2.97976, 0.09005],
            [-2.95903, -2.87265, 3.31401, 0.08349],
            [-2.68301, -2.93796, 3.68444, 0.07698],
            [-2.39858, -2.9898, 4.0, 0.07228],
            [-2.10831, -3.03028, 4.0, 0.07327],
            [-1.81414, -3.06126, 4.0, 0.07395],
            [-1.51749, -3.08428, 4.0, 0.07439],
            [-1.21933, -3.10058, 4.0, 0.07465],
            [-0.92031, -3.11128, 4.0, 0.0748],
            [-0.6208, -3.11706, 4.0, 0.07489],
            [-0.32102, -3.11848, 4.0, 0.07495],
            [-0.02111, -3.11612, 4.0, 0.07498],
            [0.27888, -3.11051, 4.0, 0.07501],
            [0.5789, -3.10214, 4.0, 0.07503],
            [0.87893, -3.09135, 3.3736, 0.08899],
            [1.17897, -3.07819, 2.93707, 0.10225],
            [1.47901, -3.06256, 2.57873, 0.11651],
            [1.77282, -3.05192, 2.29925, 0.12787],
            [2.06226, -3.04989, 2.05651, 0.14075],
            [2.34501, -3.06024, 1.82661, 0.1549],
            [2.61815, -3.08683, 1.60807, 0.17066],
            [2.87851, -3.13263, 1.39627, 0.18934],
            [3.12234, -3.20017, 1.39627, 0.1812],
            [3.34565, -3.29081, 1.39627, 0.17261],
            [3.54401, -3.40513, 1.39627, 0.16397],
            [3.71193, -3.5432, 1.39627, 0.1557],
            [3.84212, -3.7043, 1.39627, 0.14834],
            [3.92369, -3.88612, 1.44783, 0.13764],
            [3.9605, -4.07996, 1.57212, 0.1255],
            [3.95828, -4.28005, 1.58502, 0.12625],
            [3.91929, -4.48293, 1.58502, 0.13034],
            [3.83426, -4.68448, 1.75683, 0.12451],
            [3.70692, -4.87889, 1.96263, 0.11841],
            [3.54305, -5.06092, 2.20045, 0.11131],
            [3.35018, -5.22685, 2.48151, 0.10253],
            [3.13597, -5.37566, 2.71722, 0.09599],
            [2.90558, -5.50732, 2.94489, 0.09011],
            [2.66288, -5.62252, 3.16655, 0.08484],
            [2.41065, -5.7223, 3.38581, 0.08011],
            [2.15095, -5.8078, 3.60508, 0.07584],
            [1.88533, -5.88015, 3.81976, 0.07207],
            [1.61495, -5.94038, 4.0, 0.06925],
            [1.34073, -5.98937, 4.0, 0.06964],
            [1.06336, -6.0278, 4.0, 0.07],
            [0.78346, -6.05631, 4.0, 0.07034],
            [0.50155, -6.07544, 4.0, 0.07064],
            [0.2181, -6.0857, 4.0, 0.07091],
            [-0.06647, -6.08758, 4.0, 0.07114],
            [-0.35177, -6.08154, 4.0, 0.07134],
            [-0.63749, -6.06806, 4.0, 0.07151],
            [-0.92331, -6.04757, 4.0, 0.07164],
            [-1.20898, -6.02052, 4.0, 0.07174],
            [-1.49429, -5.98732, 4.0, 0.07181],
            [-1.77905, -5.94836, 4.0, 0.07185],
            [-2.06311, -5.90405, 4.0, 0.07187],
            [-2.34634, -5.85471, 4.0, 0.07187],
            [-2.62859, -5.80046, 4.0, 0.07186],
            [-2.90968, -5.74123, 3.98063, 0.07216],
            [-3.1893, -5.67657, 3.41641, 0.084],
            [-3.467, -5.60581, 3.03678, 0.09437],
            [-3.74221, -5.52812, 2.64939, 0.10794],
            [-4.01413, -5.44234, 2.64939, 0.10762],
            [-4.28163, -5.34692, 2.64939, 0.1072],
            [-4.54342, -5.2403, 2.64939, 0.10669],
            [-4.79687, -5.11901, 2.64939, 0.10606],
            [-5.03908, -4.97988, 2.64939, 0.10543],
            [-5.26523, -4.81865, 3.22465, 0.08613],
            [-5.47953, -4.64352, 3.38311, 0.08181],
            [-5.6824, -4.45649, 3.56487, 0.0774],
            [-5.87447, -4.25939, 3.58067, 0.07686],
            [-6.05563, -4.05308, 3.47638, 0.07898],
            [-6.22573, -3.83833, 3.17252, 0.08635],
            [-6.38463, -3.6158, 2.63526, 0.10376],
            [-6.53218, -3.38611, 2.50256, 0.10909],
            [-6.66792, -3.14961, 2.50256, 0.10896],
            [-6.79096, -2.90652, 2.50256, 0.10887],
            [-6.90025, -2.65704, 2.50256, 0.10884],
            [-6.99266, -2.40077, 2.50256, 0.10886],
            [-7.05986, -2.13675, 2.50256, 0.10886],
            [-7.09834, -1.86723, 2.74727, 0.0991],
            [-7.1127, -1.59531, 3.05033, 0.08927],
            [-7.10737, -1.32268, 3.31884, 0.08216],
            [-7.08533, -1.05023, 3.58546, 0.07624],
            [-7.04889, -0.77852, 3.85987, 0.07102],
            [-6.99998, -0.50788, 4.0, 0.06875],
            [-6.94025, -0.23853, 4.0, 0.06897],
            [-6.87102, 0.02942, 4.0, 0.06919],
            [-6.79312, 0.29586, 4.0, 0.0694],
            [-6.70668, 0.56057, 4.0, 0.06962],
            [-6.61151, 0.82323, 4.0, 0.06984],
            [-6.50602, 1.083, 4.0, 0.07009],
            [-6.39157, 1.33978, 4.0, 0.07028],
            [-6.2693, 1.59357, 4.0, 0.07043],
            [-6.13995, 1.84433, 4.0, 0.07054],
            [-6.00395, 2.09191, 4.0, 0.07062],
            [-5.86157, 2.33616, 4.0, 0.07068],
            [-5.71313, 2.57691, 4.0, 0.07071],
            [-5.55872, 2.81388, 4.0, 0.07071],
            [-5.39845, 3.04677, 4.0, 0.07068],
            [-5.23247, 3.2753, 4.0, 0.07061],
            [-5.06112, 3.49927, 4.0, 0.0705],
            [-4.88482, 3.7186, 4.0, 0.07035],
            [-4.70401, 3.93326, 4.0, 0.07016],
            [-4.51908, 4.14318, 3.84124, 0.07283],
            [-4.33005, 4.34786, 3.51661, 0.07923],
            [-4.13697, 4.54675, 3.02412, 0.09166],
            [-3.93978, 4.739, 2.66031, 0.10352],
            [-3.7383, 4.92335, 2.33492, 0.11696],
            [-3.53231, 5.09816, 2.05308, 0.13159],
            [-3.32162, 5.26127, 1.81038, 0.14718],
            [-3.10628, 5.41051, 1.59648, 0.16411],
            [-2.88605, 5.54136, 1.45182, 0.17645],
            [-2.6615, 5.64927, 1.3985, 0.17815],
            [-2.43398, 5.72897, 1.3985, 0.17238],
            [-2.20615, 5.77472, 1.3985, 0.16616],
            [-1.98262, 5.7806, 1.3985, 0.15989],
            [-1.77109, 5.74065, 1.3985, 0.15393],
            [-1.58206, 5.65272, 1.3985, 0.14908],
            [-1.42497, 5.52121, 1.52, 0.13478],
            [-1.29991, 5.3581, 1.72441, 0.11919],
            [-1.20291, 5.17255, 1.74363, 0.12008],
            [-1.13714, 4.96623, 1.98919, 0.10887],
            [-1.09893, 4.74477, 2.23174, 0.1007],
            [-1.08557, 4.51197, 2.32513, 0.10029],
            [-1.09519, 4.27089, 2.00717, 0.12021],
            [-1.12541, 4.02526, 1.73658, 0.14251],
            [-1.17281, 3.78049, 1.53412, 0.16252],
            [-1.20459, 3.54218, 1.53412, 0.15671],
            [-1.21672, 3.30819, 1.53412, 0.15273],
            [-1.20442, 3.08019, 1.53412, 0.14883],
            [-1.16167, 2.86076, 1.53412, 0.14572],
            [-1.08036, 2.6542, 1.53412, 0.1447],
            [-0.95003, 2.46816, 1.90267, 0.11939],
            [-0.78648, 2.29911, 2.09821, 0.1121],
            [-0.59368, 2.14728, 2.30516, 0.10646],
            [-0.37486, 2.013, 2.57475, 0.09971],
            [-0.13402, 1.89586, 2.84012, 0.0943],
            [0.1254, 1.7955, 2.85245, 0.09751],
            [0.40015, 1.71161, 2.67539, 0.10738],
            [0.68795, 1.64599, 2.50151, 0.118],
            [0.98368, 1.60127, 2.35269, 0.12713],
            [1.28044, 1.57906, 2.22715, 0.13362],
            [1.57306, 1.581, 2.11359, 0.13845],
            [1.85715, 1.60788, 2.00111, 0.1426],
            [2.12828, 1.66035, 1.88076, 0.14683],
            [2.38202, 1.7383, 1.67353, 0.15861],
            [2.61453, 1.84045, 1.50169, 0.16911],
            [2.82285, 1.96463, 1.33475, 0.1817],
            [3.00476, 2.10835, 1.33475, 0.17369],
            [3.15823, 2.26918, 1.33475, 0.16655],
            [3.28092, 2.44489, 1.33475, 0.16056],
            [3.36626, 2.63432, 1.33475, 0.15565],
            [3.40631, 2.8347, 1.33475, 0.15309],
            [3.38801, 3.04073, 1.65082, 0.1253],
            [3.32917, 3.24596, 1.86936, 0.11421],
            [3.23558, 3.44818, 2.17828, 0.10229],
            [3.11349, 3.6464, 2.36174, 0.09857],
            [2.97023, 3.84077, 2.10549, 0.11468],
            [2.81504, 4.03265, 1.84683, 0.13362],
            [2.66661, 4.23345, 1.63769, 0.15247],
            [2.53567, 4.4365, 1.45699, 0.16583],
            [2.42648, 4.64142, 1.3, 0.17861],
            [2.34209, 4.84737, 1.3, 0.17121],
            [2.28569, 5.05315, 1.3, 0.16413],
            [2.26197, 5.25687, 1.3, 0.15777],
            [2.27598, 5.45552, 1.3, 0.15319],
            [2.33458, 5.64402, 1.3, 0.15184],
            [2.44812, 5.8119, 1.51277, 0.13397],
            [2.60304, 5.9568, 1.69194, 0.12537],
            [2.79249, 6.07653, 1.88655, 0.1188],
            [3.01043, 6.1696, 2.09102, 0.11333],
            [3.25074, 6.23514, 2.29773, 0.10841],
            [3.50684, 6.27317, 2.52048, 0.10272],
            [3.77212, 6.28525, 2.67103, 0.09942],
            [4.04126, 6.27257, 2.79701, 0.09633],
            [4.3099, 6.2368, 2.92513, 0.09265],
            [4.5749, 6.18016, 2.81317, 0.09633],
            [4.83421, 6.10481, 2.59576, 0.10403],
            [5.08642, 6.01236, 2.35382, 0.11412],
            [5.33058, 5.90423, 2.35382, 0.11345],
            [5.5658, 5.78119, 2.35382, 0.11278],
            [5.7904, 5.64262, 2.35382, 0.11212],
            [6.00173, 5.48694, 2.35382, 0.11151],
            [6.19648, 5.31234, 2.35382, 0.11112],
            [6.36964, 5.1162, 2.59962, 0.10065],
            [6.52396, 4.9034, 2.80252, 0.09379],
            [6.66113, 4.67688, 2.98489, 0.08872],
            [6.78229, 4.43883, 3.19188, 0.08369],
            [6.88863, 4.19131, 3.30514, 0.08151],
            [6.98037, 3.93577, 3.40382, 0.07977],
            [7.05761, 3.67372, 3.37574, 0.08093],
            [7.12026, 3.40675, 3.26509, 0.08399],
            [7.16804, 3.13651, 3.10028, 0.08852],
            [7.20059, 2.86469, 2.89623, 0.09452],
            [7.21779, 2.59296, 2.63767, 0.10323],
            [7.21973, 2.32276, 2.33874, 0.11554],
            [7.20606, 2.05542, 2.33874, 0.11446],
            [7.17627, 1.79228, 2.33874, 0.11323],
            [7.12933, 1.53486, 2.33874, 0.11188],
            [7.0637, 1.28501, 2.33874, 0.11045],
            [6.97681, 1.04543, 2.2688, 0.11233],
            [6.86472, 0.82046, 2.2688, 0.11078],
            [6.73307, 0.60867, 2.2688, 0.10991],
            [6.58215, 0.41132, 2.2688, 0.1095],
            [6.41002, 0.23187, 2.2688, 0.1096],
            [6.21953, 0.06985, 2.2688, 0.11022],
            [6.00834, -0.06975, 2.47633, 0.10223],
            [5.78057, -0.18872, 2.67429, 0.09609],
            [5.53909, -0.28852, 2.92049, 0.08947],
            [5.28645, -0.37101, 3.11673, 0.08527],
            [5.02429, -0.43725, 3.34631, 0.08081],
            [4.75412, -0.48847, 3.61387, 0.07609],
            [4.47736, -0.52605, 3.92457, 0.07117],
            [4.19534, -0.55147, 4.0, 0.07079],
            [3.90932, -0.56626, 4.0, 0.0716],
            [3.62055, -0.57194, 4.0, 0.07221],
            [3.3303, -0.5698, 4.0, 0.07256],
            [3.04007, -0.5613, 4.0, 0.07259],
            [2.75154, -0.54779, 4.0, 0.07221],
            [2.4667, -0.53044, 4.0, 0.07134],
            [2.18764, -0.51035, 4.0, 0.06995],
            [1.91598, -0.48853, 4.0, 0.06813],
            [1.65221, -0.46573, 4.0, 0.06619],
            [1.39539, -0.44245, 4.0, 0.06447],
            [1.14351, -0.41894, 4.0, 0.06324]
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
    return myRewardObject.reward_function_z01(params, True)
    
    
    
