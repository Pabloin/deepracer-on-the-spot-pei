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


#################### RACING LINE ######################

    # Optimal racing line for the Spain track
    # Each row: [x,y,speed,timeFromPreviousPoint]
    racing_track_Spain_track = [[0.34775, -2.173, 4.0, 0.07904],
                    [0.03162, -2.17293, 4.0, 0.07903],
                    [-0.28452, -2.17311, 4.0, 0.07904],
                    [-0.60066, -2.17318, 4.0, 0.07903],
                    [-0.91682, -2.17293, 4.0, 0.07904],
                    [-1.23295, -2.17295, 4.0, 0.07903],
                    [-1.54907, -2.17315, 4.0, 0.07903],
                    [-1.86524, -2.17319, 4.0, 0.07904],
                    [-2.18141, -2.17303, 4.0, 0.07904],
                    [-2.49703, -2.17286, 4.0, 0.07891],
                    [-2.81231, -2.17287, 3.67826, 0.08571],
                    [-3.12023, -2.17178, 3.36387, 0.09154],
                    [-3.40832, -2.16639, 3.11746, 0.09243],
                    [-3.67315, -2.15481, 2.91304, 0.091],
                    [-3.91587, -2.13615, 2.74019, 0.08884],
                    [-4.13906, -2.11004, 2.59065, 0.08674],
                    [-4.34538, -2.07631, 2.46067, 0.08496],
                    [-4.53716, -2.03485, 2.34319, 0.08374],
                    [-4.71631, -1.98551, 2.23387, 0.08318],
                    [-4.88433, -1.92804, 2.13488, 0.08318],
                    [-5.04235, -1.86205, 2.13488, 0.08021],
                    [-5.19122, -1.78697, 2.13488, 0.0781],
                    [-5.33151, -1.70198, 2.13488, 0.07683],
                    [-5.46347, -1.60589, 2.13488, 0.07646],
                    [-5.587, -1.49694, 2.50447, 0.06576],
                    [-5.70146, -1.37258, 3.07226, 0.05501],
                    [-5.80898, -1.23583, 4.0, 0.04349],
                    [-5.91154, -1.09012, 4.0, 0.04455],
                    [-6.01148, -0.9397, 4.0, 0.04515],
                    [-6.0995, -0.80946, 4.0, 0.0393],
                    [-6.18728, -0.68165, 4.0, 0.03876],
                    [-6.27492, -0.55603, 4.0, 0.03829],
                    [-6.36252, -0.43242, 4.0, 0.03788],
                    [-6.45016, -0.31068, 4.0, 0.0375],
                    [-6.5379, -0.19068, 4.0, 0.03716],
                    [-6.6258, -0.07232, 4.0, 0.03686],
                    [-6.71393, 0.04449, 4.0, 0.03658],
                    [-6.80234, 0.15983, 4.0, 0.03633],
                    [-6.89109, 0.27378, 3.71387, 0.03889],
                    [-6.98023, 0.3864, 3.03045, 0.0474],
                    [-7.06985, 0.49777, 2.61858, 0.05459],
                    [-7.16, 0.60792, 2.33605, 0.06093],
                    [-7.34242, 0.82509, 2.33605, 0.12141],
                    [-7.51721, 1.0459, 2.33605, 0.12055],
                    [-7.67697, 1.27353, 2.33168, 0.11927],
                    [-7.81458, 1.51025, 2.2637, 0.12095],
                    [-7.92294, 1.75686, 2.19952, 0.12247],
                    [-7.99486, 2.012, 2.13463, 0.12418],
                    [-8.03258, 2.27135, 2.13463, 0.12278],
                    [-8.03667, 2.53161, 2.13463, 0.12194],
                    [-8.00552, 2.78942, 2.13463, 0.12165],
                    [-7.93746, 3.04073, 2.13463, 0.12197],
                    [-7.83093, 3.28049, 2.30799, 0.11368],
                    [-7.68478, 3.50219, 2.41869, 0.10979],
                    [-7.50619, 3.70355, 2.54606, 0.10571],
                    [-7.2994, 3.88253, 2.68781, 0.10175],
                    [-7.0684, 4.03801, 2.85105, 0.09767],
                    [-6.81682, 4.16957, 3.04632, 0.09319],
                    [-6.54806, 4.27741, 3.28731, 0.08809],
                    [-6.26528, 4.36241, 3.59377, 0.08216],
                    [-5.97143, 4.42617, 4.0, 0.07517],
                    [-5.6692, 4.47093, 3.70808, 0.0824],
                    [-5.36095, 4.49949, 3.02882, 0.10221],
                    [-5.04869, 4.51517, 2.62147, 0.11926],
                    [-4.73409, 4.5216, 2.34382, 0.13426],
                    [-4.41918, 4.52269, 2.13877, 0.14724],
                    [-4.14695, 4.51532, 1.97844, 0.13765],
                    [-3.91151, 4.49653, 1.84539, 0.12799],
                    [-3.7048, 4.4656, 1.7342, 0.12052],
                    [-3.5217, 4.4226, 1.63402, 0.1151],
                    [-3.35902, 4.36803, 1.45633, 0.11782],
                    [-3.21485, 4.30258, 1.45633, 0.10872],
                    [-3.08807, 4.22706, 1.45633, 0.10133],
                    [-2.97818, 4.14236, 1.45633, 0.09527],
                    [-2.88509, 4.04944, 1.45633, 0.09031],
                    [-2.80911, 3.94939, 1.45892, 0.08612],
                    [-2.75307, 3.84294, 1.45892, 0.08245],
                    [-2.71495, 3.73266, 1.51194, 0.07717],
                    [-2.69466, 3.62029, 1.56647, 0.07289],
                    [-2.69044, 3.5075, 1.62279, 0.06955],
                    [-2.7009, 3.39547, 1.68465, 0.06679],
                    [-2.72498, 3.28512, 1.75006, 0.06454],
                    [-2.76177, 3.17716, 1.82263, 0.06258],
                    [-2.81056, 3.0722, 1.89343, 0.06113],
                    [-2.87069, 2.97075, 1.99628, 0.05908],
                    [-2.94169, 2.87328, 2.11279, 0.05708],
                    [-3.02285, 2.78011, 2.24716, 0.05499],
                    [-3.11347, 2.69144, 2.40949, 0.05261],
                    [-3.21279, 2.6074, 2.60909, 0.04987],
                    [-3.32, 2.52796, 2.86347, 0.0466],
                    [-3.43416, 2.45293, 2.6432, 0.05169],
                    [-3.55428, 2.38197, 2.17238, 0.06422],
                    [-3.67924, 2.31457, 1.8861, 0.07527],
                    [-3.80787, 2.25006, 1.68759, 0.08527],
                    [-3.93614, 2.18893, 1.53879, 0.09234],
                    [-4.06004, 2.12529, 1.41938, 0.09813],
                    [-4.17613, 2.05724, 1.41938, 0.09481],
                    [-4.28186, 1.98342, 1.41938, 0.09085],
                    [-4.37538, 1.90299, 1.41938, 0.0869],
                    [-4.4553, 1.81542, 1.41938, 0.08353],
                    [-4.52032, 1.72028, 1.53686, 0.07498],
                    [-4.56869, 1.61687, 1.59239, 0.07169],
                    [-4.60276, 1.50645, 1.65207, 0.06995],
                    [-4.62264, 1.38906, 1.71608, 0.06939],
                    [-4.62773, 1.26433, 1.78799, 0.06982],
                    [-4.61657, 1.13147, 1.86957, 0.07131],
                    [-4.58656, 0.9891, 1.96042, 0.07422],
                    [-4.5332, 0.83495, 2.05988, 0.07919],
                    [-4.4483, 0.6652, 2.16004, 0.08787],
                    [-4.31593, 0.47389, 2.19343, 0.10606],
                    [-4.1156, 0.26497, 2.22222, 0.13025],
                    [-3.87159, 0.0865, 2.24818, 0.13447],
                    [-3.61395, -0.04165, 2.27402, 0.12654],
                    [-3.36566, -0.12046, 2.29642, 0.11344],
                    [-3.13683, -0.1602, 2.31769, 0.10021],
                    [-2.927, -0.17127, 2.33883, 0.08984],
                    [-2.73327, -0.16075, 2.35863, 0.08226],
                    [-2.55287, -0.13312, 2.37286, 0.07691],
                    [-2.38357, -0.09112, 2.38661, 0.07309],
                    [-2.22372, -0.0364, 2.39352, 0.07059],
                    [-2.07202, 0.03012, 2.3947, 0.06917],
                    [-1.92748, 0.10816, 2.3947, 0.06859],
                    [-1.78927, 0.19798, 2.64412, 0.06234],
                    [-1.65666, 0.3006, 2.78442, 0.06022],
                    [-1.52811, 0.41511, 2.94568, 0.05844],
                    [-1.40281, 0.54205, 3.13542, 0.05689],
                    [-1.28, 0.68231, 3.36467, 0.05541],
                    [-1.15892, 0.83709, 3.6421, 0.05395],
                    [-1.03877, 1.00792, 4.0, 0.05221],
                    [-0.91862, 1.19676, 3.68404, 0.06076],
                    [-0.79737, 1.40593, 2.94366, 0.08213],
                    [-0.67367, 1.63804, 2.51931, 0.1044],
                    [-0.54587, 1.8957, 2.23675, 0.12859],
                    [-0.41214, 2.1805, 2.03055, 0.15495],
                    [-0.27186, 2.45834, 1.86713, 0.1667],
                    [-0.11843, 2.71914, 1.73627, 0.17427],
                    [0.05252, 2.95406, 1.73627, 0.16733],
                    [0.24282, 3.1558, 1.73627, 0.15973],
                    [0.4523, 3.31851, 1.73627, 0.15277],
                    [0.6794, 3.4369, 1.73627, 0.1475],
                    [0.92148, 3.50479, 1.95437, 0.12864],
                    [1.17407, 3.51372, 2.11404, 0.11956],
                    [1.42993, 3.47367, 2.31717, 0.11176],
                    [1.68478, 3.38833, 2.5896, 0.10378],
                    [1.9352, 3.26155, 2.98246, 0.09411],
                    [2.1787, 3.09844, 3.62855, 0.08077],
                    [2.41403, 2.90595, 4.0, 0.07601],
                    [2.64178, 2.69291, 4.0, 0.07796],
                    [2.86447, 2.46933, 4.0, 0.07889],
                    [3.08676, 2.2447, 3.22907, 0.09787],
                    [3.30934, 2.02005, 2.65999, 0.11889],
                    [3.53187, 1.79508, 2.31065, 0.13695],
                    [3.75427, 1.56983, 2.06878, 0.15301],
                    [3.97641, 1.34721, 1.88874, 0.16651],
                    [4.19715, 1.14479, 1.74488, 0.17164],
                    [4.41321, 0.97574, 1.62782, 0.16853],
                    [4.61966, 0.84634, 1.53154, 0.15909],
                    [4.81352, 0.75553, 1.44494, 0.14816],
                    [4.99381, 0.69892, 1.36805, 0.13812],
                    [5.16051, 0.67175, 1.3, 0.12993],
                    [5.31387, 0.67004, 1.3, 0.11798],
                    [5.45403, 0.69082, 1.3, 0.10899],
                    [5.58085, 0.73199, 1.3, 0.10257],
                    [5.69365, 0.79243, 1.3, 0.09844],
                    [5.79096, 0.87188, 1.37873, 0.09112],
                    [5.87004, 0.97096, 1.47004, 0.08624],
                    [5.93072, 1.08736, 1.57685, 0.08325],
                    [5.97211, 1.21983, 1.71094, 0.08111],
                    [5.99266, 1.36774, 1.88391, 0.07927],
                    [5.99044, 1.5307, 2.12066, 0.07685],
                    [5.96345, 1.70826, 2.46894, 0.07274],
                    [5.91045, 1.89955, 2.27125, 0.0874],
                    [5.83221, 2.10287, 2.02895, 0.10737],
                    [5.7335, 2.31514, 1.85064, 0.1265],
                    [5.63686, 2.50726, 1.70721, 0.12597],
                    [5.55635, 2.69304, 1.59134, 0.12724],
                    [5.49578, 2.87069, 1.4939, 0.12564],
                    [5.45645, 3.03926, 1.40987, 0.12278],
                    [5.4382, 3.19832, 1.33463, 0.11996],
                    [5.44032, 3.34759, 1.33463, 0.11186],
                    [5.46216, 3.48672, 1.33463, 0.10552],
                    [5.50334, 3.61508, 1.33463, 0.101],
                    [5.56401, 3.73161, 1.33463, 0.09844],
                    [5.64513, 3.83446, 1.65679, 0.07906],
                    [5.74889, 3.92024, 1.73875, 0.07743],
                    [5.86816, 3.99315, 1.83096, 0.07635],
                    [6.00303, 4.05237, 1.93405, 0.07616],
                    [6.15417, 4.09658, 2.05482, 0.07664],
                    [6.32298, 4.12377, 2.19828, 0.07778],
                    [6.5118, 4.13106, 2.31507, 0.08162],
                    [6.72455, 4.11405, 2.29787, 0.09288],
                    [6.96924, 4.06504, 2.27981, 0.10946],
                    [7.23605, 3.97246, 2.25811, 0.12507],
                    [7.43782, 3.87107, 2.2331, 0.10112],
                    [7.60293, 3.76378, 2.20505, 0.0893],
                    [7.74238, 3.65197, 2.20505, 0.08106],
                    [7.86188, 3.5364, 2.20505, 0.07539],
                    [7.96479, 3.41757, 2.20505, 0.07129],
                    [8.05322, 3.29577, 2.20505, 0.06826],
                    [8.12853, 3.17115, 2.38864, 0.06096],
                    [8.19155, 3.04381, 2.59316, 0.05479],
                    [8.2447, 2.91427, 2.85739, 0.049],
                    [8.28972, 2.78301, 3.21281, 0.04319],
                    [8.32812, 2.65059, 3.74461, 0.03682],
                    [8.3613, 2.51757, 4.0, 0.03427],
                    [8.39063, 2.38441, 4.0, 0.03409],
                    [8.41744, 2.25135, 4.0, 0.03393],
                    [8.44605, 2.11888, 4.0, 0.03388],
                    [8.47641, 1.98572, 4.0, 0.03414],
                    [8.5082, 1.85198, 4.0, 0.03437],
                    [8.54111, 1.71779, 4.0, 0.03454],
                    [8.57477, 1.58329, 3.88727, 0.03567],
                    [8.60883, 1.44862, 3.55754, 0.03905],
                    [8.64619, 1.29642, 3.29481, 0.04757],
                    [8.68404, 1.13291, 3.10924, 0.05398],
                    [8.72093, 0.95736, 2.94774, 0.06086],
                    [8.7547, 0.77082, 2.8059, 0.06756],
                    [8.78272, 0.57589, 2.67642, 0.07358],
                    [8.80238, 0.37615, 2.55908, 0.07843],
                    [8.81154, 0.17535, 2.45225, 0.08197],
                    [8.80892, -0.0233, 2.35362, 0.08441],
                    [8.79385, -0.21739, 2.26053, 0.08612],
                    [8.76608, -0.40519, 2.17117, 0.08744],
                    [8.72555, -0.58546, 2.0881, 0.08848],
                    [8.67236, -0.75727, 2.0881, 0.08613],
                    [8.60661, -0.91991, 2.0881, 0.08401],
                    [8.52835, -1.07276, 2.0881, 0.08224],
                    [8.43746, -1.2152, 2.0881, 0.08092],
                    [8.33356, -1.34653, 2.27364, 0.07365],
                    [8.2158, -1.4659, 2.37408, 0.07063],
                    [8.08601, -1.57512, 2.48104, 0.06837],
                    [7.94437, -1.67477, 2.60203, 0.06655],
                    [7.79071, -1.76521, 2.73873, 0.0651],
                    [7.62452, -1.84667, 2.8987, 0.06385],
                    [7.44497, -1.91922, 3.0896, 0.06268],
                    [7.25094, -1.98282, 3.32007, 0.0615],
                    [7.04109, -2.03732, 3.60931, 0.06007],
                    [6.81386, -2.08251, 3.98257, 0.05817],
                    [6.56783, -2.11817, 4.0, 0.06215],
                    [6.30214, -2.14423, 4.0, 0.06674],
                    [6.01745, -2.16104, 4.0, 0.0713],
                    [5.71684, -2.16974, 4.0, 0.07518],
                    [5.40604, -2.17253, 4.0, 0.0777],
                    [5.08989, -2.17261, 4.0, 0.07904],
                    [4.77373, -2.173, 4.0, 0.07904],
                    [4.45759, -2.17311, 4.0, 0.07903],
                    [4.14147, -2.17298, 4.0, 0.07903],
                    [3.82532, -2.17289, 4.0, 0.07904],
                    [3.50917, -2.17299, 4.0, 0.07904],
                    [3.19303, -2.17314, 4.0, 0.07903],
                    [2.87689, -2.1731, 4.0, 0.07904],
                    [2.56075, -2.17295, 4.0, 0.07903],
                    [2.2446, -2.17299, 4.0, 0.07904],
                    [1.92847, -2.17312, 4.0, 0.07903],
                    [1.61233, -2.17306, 4.0, 0.07904],
                    [1.29618, -2.17296, 4.0, 0.07904],
                    [0.98004, -2.17304, 4.0, 0.07903],
                    [0.6639, -2.17313, 4.0, 0.07904]]
                    

#################### RACING LINE - END ######################



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


        # Rogue Raceway  aka  2022_march_pro
        # Optimal racing line, debería ser:
        # Each row: [x,y,speed,timeFromPreviousPoint]
        racing_track = [
            [ 6.32350560e-01, -3.88212448e-01 ],
            [ 8.95432720e-01, -4.68818002e-01 ],
            [ 1.15943611e+00, -5.42195235e-01 ],
            [ 1.42436073e+00, -6.08344148e-01 ],
            [ 1.69020658e+00, -6.67264741e-01 ],
            [ 1.95697366e+00, -7.18957013e-01 ],
            [ 2.22466197e+00, -7.63420965e-01 ],
            [ 2.49327151e+00, -8.00656596e-01 ],
            [ 2.76280228e+00, -8.30663907e-01 ],
            [ 3.03325428e+00, -8.53442897e-01 ],
            [ 3.30462751e+00, -8.68993567e-01 ],
            [ 3.57692197e+00, -8.77315916e-01 ],
            [ 3.85013767e+00, -8.78409945e-01 ],
            [ 4.12427459e+00, -8.72275654e-01 ],
            [ 4.39933274e+00, -8.58913042e-01 ],
            [ 4.67531212e+00, -8.38322109e-01 ],
            [ 4.95101825e+00, -8.08611414e-01 ],
            [ 5.21825688e+00, -7.56805507e-01 ],
            [ 5.47547547e+00, -6.80445937e-01 ],
            [ 5.72267399e+00, -5.79532704e-01 ],
            [ 5.95985247e+00, -4.54065808e-01 ],
            [ 6.18701089e+00, -3.04045250e-01 ],
            [ 6.40414926e+00, -1.29471028e-01 ],
            [ 6.61104421e+00,  6.93744769e-02 ],
            [ 6.79978109e+00,  2.82485196e-01 ],
            [ 6.96642063e+00,  5.04880938e-01 ],
            [ 7.11096283e+00,  7.36561704e-01 ],
            [ 7.23340768e+00,  9.77527494e-01 ],
            [ 7.33375520e+00,  1.22777831e+00 ],
            [ 7.41200537e+00,  1.48731414e+00 ],
            [ 7.46815821e+00,  1.75613500e+00 ],
            [ 7.50221370e+00,  2.03424089e+00 ],
            [ 7.51422913e+00,  2.32144713e+00 ],
            [ 7.50722825e+00,  2.60800699e+00 ],
            [ 7.48292433e+00,  2.88839783e+00 ],
            [ 7.44131737e+00,  3.16261965e+00 ],
            [ 7.38240737e+00,  3.43067245e+00 ],
            [ 7.30619433e+00,  3.69255623e+00 ],
            [ 7.21267826e+00,  3.94827099e+00 ],
            [ 7.10185915e+00,  4.19781674e+00 ],
            [ 6.97373700e+00,  4.44119346e+00 ],
            [ 6.82831181e+00,  4.67840116e+00 ],
            [ 6.66558359e+00,  4.90943985e+00 ],
            [ 6.48560186e+00,  5.13406868e+00 ],
            [ 6.29027536e+00,  5.34300755e+00 ],
            [ 6.08058266e+00,  5.53149877e+00 ],
            [ 5.85652375e+00,  5.69954236e+00 ],
            [ 5.61809862e+00,  5.84713830e+00 ],
            [ 5.36530729e+00,  5.97428661e+00 ],
            [ 5.09814976e+00,  6.08098727e+00 ],
            [ 4.81662601e+00,  6.16724029e+00 ],
            [ 4.52073605e+00,  6.23304568e+00 ],
            [ 4.21047989e+00,  6.27840342e+00 ],
            [ 3.88585751e+00,  6.30331353e+00 ],
            [ 3.54686893e+00,  6.30777599e+00 ],
            [ 3.19846287e+00,  6.29043966e+00 ],
            [ 2.88442936e+00,  6.23934847e+00 ],
            [ 2.61506149e+00,  6.15169209e+00 ],
            [ 2.39035926e+00,  6.02747052e+00 ],
            [ 2.21032267e+00,  5.86668376e+00 ],
            [ 2.07495170e+00,  5.66933182e+00 ],
            [ 1.98424638e+00,  5.43541469e+00 ],
            [ 1.93820669e+00,  5.16493236e+00 ],
            [ 1.93684166e+00,  4.85795071e+00 ],
            [ 1.98651122e+00,  4.56088667e+00 ],
            [ 2.09267819e+00,  4.31360986e+00 ],
            [ 2.25534258e+00,  4.11612030e+00 ],
            [ 2.47450440e+00,  3.96841798e+00 ],
            [ 2.75016363e+00,  3.87050291e+00 ],
            [ 3.08232027e+00,  3.82237507e+00 ],
            [ 3.41744145e+00,  3.78295625e+00 ],
            [ 3.68073018e+00,  3.69485137e+00 ],
            [ 3.87168328e+00,  3.55767429e+00 ],
            [ 3.99030073e+00,  3.37142500e+00 ],
            [ 4.03658253e+00,  3.13610351e+00 ],
            [ 4.01052870e+00,  2.85170981e+00 ],
            [ 3.91708985e+00,  2.52977821e+00 ],
            [ 3.78945598e+00,  2.24763690e+00 ],
            [ 3.63378358e+00,  2.01962962e+00 ],
            [ 3.45007263e+00,  1.84575637e+00 ],
            [ 3.23832314e+00,  1.72601715e+00 ],
            [ 2.99853511e+00,  1.66041196e+00 ],
            [ 2.73070854e+00,  1.64894080e+00 ],
            [ 2.43484342e+00,  1.69160367e+00 ],
            [ 2.12567806e+00,  1.76017346e+00 ],
            [ 1.82284106e+00,  1.81705703e+00 ],
            [ 1.52642986e+00,  1.86206780e+00 ],
            [ 1.23644445e+00,  1.89520576e+00 ],
            [ 9.52884822e-01,  1.91647092e+00 ],
            [ 6.75750986e-01,  1.92586327e+00 ],
            [ 4.05042940e-01,  1.92338282e+00 ],
            [ 1.40760683e-01,  1.90902957e+00 ],
            [-1.21395629e-01,  1.88647803e+00 ],
            [-3.89980426e-01,  1.86303855e+00 ],
            [-6.65228573e-01,  1.83891186e+00 ],
            [-9.47140070e-01,  1.81409794e+00 ],
            [-1.20485814e+00,  1.83475076e+00 ],
            [-1.37425587e+00,  1.99678799e+00 ],
            [-1.45502337e+00,  2.29689403e+00 ],
            [-1.47864237e+00,  2.61686061e+00 ],
            [-1.45704828e+00,  2.91187246e+00 ],
            [-1.39024109e+00,  3.18192957e+00 ],
            [-1.27887839e+00,  3.42735566e+00 ],
            [-1.17162496e+00,  3.67210649e+00 ],
            [-1.09866651e+00,  3.93104132e+00 ],
            [-1.06000304e+00,  4.20416014e+00 ],
            [-1.05563457e+00,  4.49146296e+00 ],
            [-1.08556108e+00,  4.79294977e+00 ],
            [-1.14978258e+00,  5.10862058e+00 ],
            [-1.24829907e+00,  5.43847539e+00 ],
            [-1.37414027e+00,  5.76275095e+00 ],
            [-1.51126800e+00,  6.03597305e+00 ],
            [-1.65904492e+00,  6.25633470e+00 ],
            [-1.81747104e+00,  6.42383589e+00 ],
            [-1.98654637e+00,  6.53847662e+00 ],
            [-2.16627089e+00,  6.60025690e+00 ],
            [-2.35664462e+00,  6.60917672e+00 ],
            [-2.55766754e+00,  6.56523608e+00 ],
            [-2.76933967e+00,  6.46843498e+00 ],
            [-2.99166100e+00,  6.31877342e+00 ],
            [-3.22463153e+00,  6.11625141e+00 ],
            [-3.46704631e+00,  5.86453552e+00 ],
            [-3.70433269e+00,  5.60796927e+00 ],
            [-3.93220875e+00,  5.35958220e+00 ],
            [-4.15067451e+00,  5.11937430e+00 ],
            [-4.35972996e+00,  4.88734556e+00 ],
            [-4.55937510e+00,  4.66349600e+00 ],
            [-4.74960993e+00,  4.44782560e+00 ],
            [-4.93043445e+00,  4.24033437e+00 ],
            [-5.10397432e+00,  4.03637659e+00 ],
            [-5.27362953e+00,  3.82852139e+00 ],
            [-5.43944457e+00,  3.61667156e+00 ],
            [-5.60141941e+00,  3.40082712e+00 ],
            [-5.75955408e+00,  3.18098805e+00 ],
            [-5.91384857e+00,  2.95715436e+00 ],
            [-6.06430287e+00,  2.72932605e+00 ],
            [-6.21091700e+00,  2.49750312e+00 ],
            [-6.35365721e+00,  2.26168324e+00 ],
            [-6.48891910e+00,  2.02161787e+00 ],
            [-6.61427625e+00,  1.77713969e+00 ],
            [-6.72972865e+00,  1.52824872e+00 ],
            [-6.83527632e+00,  1.27494493e+00 ],
            [-6.93091924e+00,  1.01722835e+00 ],
            [-7.01665742e+00,  7.55098956e-01 ],
            [-7.09249087e+00,  4.88556761e-01 ],
            [-7.15841957e+00,  2.17601763e-01 ],
            [-7.21444353e+00, -5.77660399e-02 ],
            [-7.26056274e+00, -3.37546647e-01 ],
            [-7.29677722e+00, -6.21740057e-01 ],
            [-7.32308696e+00, -9.10346272e-01 ],
            [-7.33949195e+00, -1.20336529e+00 ],
            [-7.34599221e+00, -1.50079711e+00 ],
            [-7.34258772e+00, -1.80264174e+00 ],
            [-7.32927849e+00, -2.10889917e+00 ],
            [-7.30602438e+00, -2.41944782e+00 ],
            [-7.26907459e+00, -2.72292786e+00 ],
            [-7.21597420e+00, -3.01190417e+00 ],
            [-7.14672320e+00, -3.28637674e+00 ],
            [-7.06132160e+00, -3.54634558e+00 ],
            [-6.95976939e+00, -3.79181068e+00 ],
            [-6.84206658e+00, -4.02277205e+00 ],
            [-6.70821316e+00, -4.23922968e+00 ],
            [-6.55820913e+00, -4.44118358e+00 ],
            [-6.39205450e+00, -4.62863375e+00 ],
            [-6.20974927e+00, -4.80158018e+00 ],
            [-6.01129343e+00, -4.96002287e+00 ],
            [-5.79668698e+00, -5.10396183e+00 ],
            [-5.56592993e+00, -5.23339706e+00 ],
            [-5.31902228e+00, -5.34832855e+00 ],
            [-5.05624476e+00, -5.44896183e+00 ],
            [-4.78734294e+00, -5.54243118e+00 ],
            [-4.51713121e+00, -5.63226104e+00 ],
            [-4.24560959e+00, -5.71845139e+00 ],
            [-3.97277807e+00, -5.80100223e+00 ],
            [-3.69863665e+00, -5.87991357e+00 ],
            [-3.42318533e+00, -5.95518541e+00 ],
            [-3.14642411e+00, -6.02681775e+00 ],
            [-2.86835300e+00, -6.09481058e+00 ],
            [-2.58897198e+00, -6.15916391e+00 ],
            [-2.30828106e+00, -6.21987774e+00 ],
            [-2.02628025e+00, -6.27695206e+00 ],
            [-1.74296954e+00, -6.33038688e+00 ],
            [-1.45834893e+00, -6.38018219e+00 ],
            [-1.17241842e+00, -6.42633801e+00 ],
            [-8.85178008e-01, -6.46885432e+00 ],
            [-5.96627700e-01, -6.50773112e+00 ],
            [-3.06767493e-01, -6.54296843e+00 ],
            [-1.56770178e-02, -6.57441653e+00 ],
            [ 2.72497782e-01, -6.59428162e+00 ],
            [ 5.55417167e-01, -6.59816530e+00 ],
            [ 8.33081137e-01, -6.58606757e+00 ],
            [ 1.10548969e+00, -6.55798843e+00 ],
            [ 1.37264283e+00, -6.51392788e+00 ],
            [ 1.63454056e+00, -6.45388592e+00 ],
            [ 1.89118287e+00, -6.37786254e+00 ],
            [ 2.14256976e+00, -6.28585776e+00 ],
            [ 2.38870124e+00, -6.17787157e+00 ],
            [ 2.62957731e+00, -6.05390397e+00 ],
            [ 2.86519796e+00, -5.91395495e+00 ],
            [ 3.09556319e+00, -5.75802453e+00 ],
            [ 3.32067301e+00, -5.58611269e+00 ],
            [ 3.54052742e+00, -5.39821945e+00 ],
            [ 3.75512641e+00, -5.19434479e+00 ],
            [ 3.93986477e+00, -4.97567950e+00 ],
            [ 4.05918358e+00, -4.74394445e+00 ],
            [ 4.11279393e+00, -4.49915363e+00 ],
            [ 4.10069583e+00, -4.24130703e+00 ],
            [ 4.02288926e+00, -3.97040466e+00 ],
            [ 3.87965504e+00, -3.68692812e+00 ],
            [ 3.69633545e+00, -3.43434087e+00 ],
            [ 3.48939191e+00, -3.24087518e+00 ],
            [ 3.25882442e+00, -3.10653108e+00 ],
            [ 3.00463298e+00, -3.03130854e+00 ],
            [ 2.72900322e+00, -3.01041817e+00 ],
            [ 2.45149296e+00, -3.00100243e+00 ],
            [ 2.17673970e+00, -2.99289908e+00 ],
            [ 1.90474344e+00, -2.98610812e+00 ],
            [ 1.63550418e+00, -2.98062954e+00 ],
            [ 1.36902192e+00, -2.97646334e+00 ],
            [ 1.10295617e+00, -2.97506274e+00 ],
            [ 8.32997953e-01, -2.97910320e+00 ],
            [ 5.59053411e-01, -2.98864298e+00 ],
            [ 2.81122548e-01, -3.00368208e+00 ],
            [-7.94636103e-04, -3.02422051e+00 ],
            [-2.86698142e-01, -3.05025826e+00 ],
            [-5.76587968e-01, -3.08179533e+00 ],
            [-8.70464116e-01, -3.11883173e+00 ],
            [-1.16832659e+00, -3.16136745e+00 ],
            [-1.47017538e+00, -3.20940250e+00 ],
            [-1.77601049e+00, -3.26293687e+00 ],
            [-2.08553612e+00, -3.32142581e+00 ],
            [-2.38547228e+00, -3.36041224e+00 ],
            [-2.66865682e+00, -3.36670605e+00 ],
            [-2.93508974e+00, -3.34030723e+00 ],
            [-3.18477105e+00, -3.28121579e+00 ],
            [-3.41770075e+00, -3.18943172e+00 ],
            [-3.63387883e+00, -3.06495503e+00 ],
            [-3.83330529e+00, -2.90778571e+00 ],
            [-4.01598014e+00, -2.71792376e+00 ],
            [-4.18190337e+00, -2.49536919e+00 ],
            [-4.33107499e+00, -2.24012199e+00 ],
            [-4.46349499e+00, -1.95218217e+00 ],
            [-4.57916338e+00, -1.63154972e+00 ],
            [-4.66644298e+00, -1.30628012e+00 ],
            [-4.70803751e+00, -1.01807209e+00 ],
            [-4.70378470e+00, -7.67316846e-01 ],
            [-4.65368456e+00, -5.54014394e-01 ],
            [-4.55773707e+00, -3.78164734e-01 ],
            [-4.41594224e+00, -2.39767864e-01 ],
            [-4.22830007e+00, -1.38823786e-01 ],
            [-3.99481056e+00, -7.53324991e-02 ],
            [-3.71547370e+00, -4.92940032e-02 ],
            [-3.39065704e+00, -6.04481205e-02 ],
            [-3.05365598e+00, -8.52248442e-02 ],
            [-2.72611622e+00, -1.08301068e-01 ],
            [-2.40803775e+00, -1.29676791e-01 ],
            [-2.09942058e+00, -1.49352014e-01 ],
            [-1.80026471e+00, -1.67326737e-01 ],
            [-1.51057013e+00, -1.83600960e-01 ],
            [-1.23033684e+00, -1.98174682e-01 ],
            [-9.59564856e-01, -2.11047905e-01 ],
            [-6.96752105e-01, -2.23448150e-01 ],
            [-4.33752088e-01, -2.42032960e-01 ],
            [-1.69341813e-01, -2.67801794e-01 ],
            [ 9.64787202e-02, -3.00754653e-01 ],
            [ 3.63709511e-01, -3.40891538e-01 ],
            [ 6.32350560e-01, -3.88212448e-01 ]
        ]





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
            # print("=== Speed reward (w/out multiple): %f ===" % speed_reward)
            # print("Direction difference: %f" % direction_diff)
            print("Predicted time: %f" % projected_time)
            # print("=== Steps reward: %f ===" % steps_reward)
            # print("=== Finish reward: %f ===" % finish_reward)
            
        #################### RETURN REWARD ####################
        return float(reward)



myRewardObject = MyRewardClassZ01() 

def reward_function(params):
    return myRewardObject.reward_function_z01(params)
    
    
    
