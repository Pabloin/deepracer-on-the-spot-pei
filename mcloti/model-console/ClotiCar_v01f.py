import math

# Track DBro Super Raceway (2022_july_pro_cw)
#       57.89 meters	
#       1.07 meters

PRINT_LOG = False

class CarControl:

    Recta = "Recta"
    Curva = "Curva"
    DIR_L = "DIR_L"
    DIR_C = "DIR_C"
    DIR_R = "DIR_R"

    Ctrl_ON  = "_ON"
    Ctrl_OFF = "OFF"

    Tramo_01 = [ Ctrl_OFF, Recta, DIR_C, 0,1,2,3,4,5 ]
    Tramo_02 = [ Ctrl_OFF, Curva, DIR_R, 6,7,8,9,10,11,12 ]
    Tramo_03 = [ Ctrl_OFF, Recta, DIR_C, 13,14,15,16,17,18,19,20,21,22,23 ]
    Tramo_04 = [ Ctrl_OFF, Curva, DIR_R, 24,25,26,27,28,29,30 ]
    Tramo_05 = [ Ctrl_OFF, Curva, DIR_R, 31,32,33,34,35,36 ]
    Tramo_06 = [ Ctrl_OFF, Recta, DIR_C, 37,38,39,40,41,42 ]
    Tramo_07 = [ Ctrl_OFF, Curva, DIR_L, 43,44,45,46,47,48 ]
    Tramo_08 = [ Ctrl_OFF, Recta, DIR_C, 49,50,51,52,53,54,55,56,57,58,59,60,61 ]
    Tramo_09 = [ Ctrl_ON,  Curva, DIR_L, 62,63,64,65,66 ]
    Tramo_10 = [ Ctrl_OFF, Curva, DIR_R, 67,68,69,70,71,72,73 ]
    Tramo_11 = [ Ctrl_OFF, Curva, DIR_R, 74,75,76,77,78,79 ]
    Tramo_12 = [ Ctrl_OFF, Recta, DIR_C, 80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99 ]
    Tramo_13 = [ Ctrl_OFF, Curva, DIR_R, 100,101,102,103,104,105,106,107,108,109 ]
    Tramo_14 = [ Ctrl_OFF, Recta, DIR_C, 110,111,112,113,114,115,116,117,118,119 ]
    Tramo_15 = [ Ctrl_OFF, Curva, DIR_R, 120,121,122,123,124,125,126 ]
    Tramo_16 = [ Ctrl_OFF, Recta, DIR_C, 127,128,129,130,131,132,133,134,135,136,137,138,139 ]
    Tramo_17 = [ Ctrl_OFF, Curva, DIR_R, 140,141,142,143 ]
    Tramo_18 = [ Ctrl_OFF, Recta, DIR_C, 144,145,146,147,148,149 ]
    Tramo_19 = [ Ctrl_ON,  Curva, DIR_L, 150,151,152,153,154,155,156,157,158,159 ]
    Tramo_20 = [ Ctrl_OFF, Recta, DIR_C, 160,161,162,163,164,165,166,167,168,169 ]
    Tramo_21 = [ Ctrl_OFF, Curva, DIR_L, 170,171,172,173,174,175 ]
    Tramo_22 = [ Ctrl_OFF, Recta, DIR_C, 176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194 ]

    Tramos = [
        Tramo_01, Tramo_02, Tramo_03, Tramo_04, Tramo_05, 
        Tramo_06, Tramo_07, Tramo_08, Tramo_09, Tramo_10, 
        Tramo_11, Tramo_12, Tramo_13, Tramo_14, Tramo_15, 
        Tramo_16, Tramo_17, Tramo_18, Tramo_19, Tramo_20, 
        Tramo_21, Tramo_22
    ]


    # Si el control esta Ctrl_OFF, la función de dirección retorna Ok
    # si el control esta ON y coincide esta OK, sino False
    @staticmethod
    def direccion_ok(waypoint, dir):

        for t in CarControl.Tramos:
            if (waypoint in t):
                is_off = (CarControl.Ctrl_OFF  in t)   
                dir_ok = (dir in t)
                if PRINT_LOG:
                   print(f"direccion_ok({waypoint},{dir})={t} esta la dir en el tramo? {dir_ok}")
                if (is_off):
                    return True
                return dir_ok

        return False

    @staticmethod
    def aux_side(params):

        is_left_of_center    = params['is_left_of_center']
        distance_from_center = params['distance_from_center']

        MARK_01 = 0.10

        if distance_from_center < MARK_01:
            return CarControl.DIR_C
        
        return CarControl.DIR_L if is_left_of_center else CarControl.DIR_R




def aux_heading_vs_track_angle(params):

    # Params for heading eval
    track_waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    
    # Heading and track_angle closer
    wp0_xy = track_waypoints[closest_waypoints[0]]
    wp1_xy = track_waypoints[closest_waypoints[1]]

    heading = params['heading']
    
    track_angle = math.degrees(math.atan2(wp1_xy[1] - wp0_xy[1], wp1_xy[0] - wp0_xy[0]))

    angleDiffernce = abs(track_angle - heading)

    if angleDiffernce > 180:
       angleDiffernce = 360 - angleDiffernce

    return angleDiffernce



def reward_function(params):

    # Params for borders eval
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    is_offtrack = params['is_offtrack']

    # Params for steering eval
    abs_steering = abs(params['steering_angle'])


    # Speed y Progreso
    speed = params['speed']
    progress = params['progress']



    REWARD_ZERO = 1e-3

    # Give a very low reward by default
    reward = 1e-3

    # Si Off track Retorna Zero
    if is_offtrack:
        return REWARD_ZERO

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0


    # Penalize reward if the car is steering too much
    ABS_STEERING_UMBRAL = 15
    if abs_steering > ABS_STEERING_UMBRAL:
        reward *= 0.8


    # Penalize reward heading vs track is high
    ABS_ANGLE_DIFF_UMBRAL = 10

    angleDiffernce = aux_heading_vs_track_angle(params)

    if angleDiffernce > ABS_ANGLE_DIFF_UMBRAL:
        reward *= 0.7


    # Penalize reward si la direccion del auto (L, C, R) esta lejos del desado para el tramo
    # En este caso, solo en el tramo de Waypoints (62,63,64,65,66) y Left

    closest_waypoints = params['closest_waypoints']
    wp_Cerca0 = closest_waypoints[0]
    wp_Cerca1 = closest_waypoints[1]

    dir = CarControl.aux_side(params)

    if not CarControl.direccion_ok(wp_Cerca1, dir):
        reward *= 0.8

    
    # Speed y Progreso
    SPEED_UMBRAL = 3
    if speed < SPEED_UMBRAL:
        reward *= 0.8
    if progress == 100:    
        reward += 100

    return float(reward)


   
##
# Similar a:
# https://www.linkedin.com/pulse/samples-reward-functions-aws-deepracer-bahman-javadi
# y a un par de:
    # https://refactored.ai/microcourse/notebook?path=content%2FDeepRacer%2FAWS_DeepRacer_Reward_function_Additional_material.ipynb
    # IDEM TO
    # https://wiki.deepracing.io/Training_the_AWS_DeepRacer
# Y contiene a:
#    https://github.com/sasasavic82/deepracer-reward/blob/master/model/reward_v1.py



# Nota ... la otra corriente de la hipotenusa es
#    https://everdark.github.io/k9/projects/deepracer_2020/deepracer_2020.html
# que esta mas claro en:
#    https://wiki.deepracing.io/Training_the_AWS_DeepRacer
#

        # rabbit = [waypoints[closest_waypoints+1][0],waypoints[closest_waypoints+1][1]]

        # radius = math.hypot(x - rabbit[0], y - rabbit[1])

        # pointing[0] = x + (radius * math.cos(car_orientation))
        # pointing[1] = y + (radius * math.sin(car_orientation))

        # vector_delta = math.hypot(pointing[0] - rabbit[0], pointing[1] - rabbit[1])




# De un Post borrado pero con Time Machine
#
# (B-Sharp)
# https://medium.com/proud2becloud/deepracer-our-journey-to-the-top-ten-257ff69922e
# https://web.archive.org/web/20200905141829/https://medium.com/proud2becloud/deepracer-our-journey-to-the-top-ten-257ff69922e
#
# Hoping that there will soon be new opportunities to get on track, we want to share some of our notes with you:

# It is better to use a machine learning model specific to the track on which you want to compete;
# It is not strictly necessary to train a model for more than eight consecutive hours but, to obtain record times, it becomes essential;
# It is always possible to increase confidence by changing the car’s degrees of freedom;
# Using Waypoints allows you to outline the ideal path;
# To gain those thousandths of a second that make the difference, you can manually vary the speed of the machine during the laps.


