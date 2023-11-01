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

    Tramo_01 = [ Ctrl_ON,  Recta, DIR_C, 0,1,2,3,4,5 ]
    Tramo_02 = [ Ctrl_ON,  Curva, DIR_R, 6,7,8,9,10,11,12 ]
    Tramo_03 = [ Ctrl_OFF, Recta, DIR_C, 13,14,15,16,17,18,19,20,21,22,23 ]
    Tramo_04 = [ Ctrl_OFF, Curva, DIR_R, 24,25,26,27,28,29,30 ]
    Tramo_05 = [ Ctrl_OFF, Curva, DIR_R, 31,32,33,34,35,36 ]
    Tramo_06 = [ Ctrl_OFF, Recta, DIR_C, 37,38,39,40,41,42 ]
    Tramo_07 = [ Ctrl_OFF, Curva, DIR_L, 43,44,45,46,47,48 ]
    Tramo_08 = [ Ctrl_OFF, Recta, DIR_C, 49,50,51,52,53,54,55,56,57,58,59,60,61 ]
    Tramo_09 = [ Ctrl_ON,  Curva, DIR_L, 62,63,64,65,66 ]
    Tramo_10 = [ Ctrl_ON,  Curva, DIR_R, 67,68,69,70,71,72,73 ]
    Tramo_11 = [ Ctrl_ON,  Curva, DIR_R, 74,75,76,77,78,79 ]
    Tramo_12 = [ Ctrl_ON,  Recta, DIR_C, 80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99 ]
    Tramo_13 = [ Ctrl_ON,  Curva, DIR_R, 100,101,102,103,104,105,106,107,108,109 ]
    Tramo_14 = [ Ctrl_OFF, Recta, DIR_C, 110,111,112,113,114,115,116,117,118,119 ]
    Tramo_15 = [ Ctrl_OFF, Curva, DIR_R, 120,121,122,123,124,125,126 ]
    Tramo_16 = [ Ctrl_OFF, Recta, DIR_C, 127,128,129,130,131,132,133,134,135,136,137,138,139 ]
    Tramo_17 = [ Ctrl_OFF, Curva, DIR_R, 140,141,142,143 ]
    Tramo_18 = [ Ctrl_OFF, Recta, DIR_C, 144,145,146,147,148,149 ]
    Tramo_19 = [ Ctrl_ON,  Curva, DIR_L, 150,151,152,153,154,155,156,157,158,159 ]
    Tramo_20 = [ Ctrl_ON, Recta, DIR_C, 160,161,162,163,164,165,166,167,168,169 ]
    Tramo_21 = [ Ctrl_OFF, Curva, DIR_R, 170,171,172,173,174,175 ]
    Tramo_22 = [ Ctrl_ON,  Recta, DIR_C, 176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194 ]

    Tramos = [
        Tramo_01, Tramo_02, Tramo_03, Tramo_04, Tramo_05, 
        Tramo_06, Tramo_07, Tramo_08, Tramo_09, Tramo_10, 
        Tramo_11, Tramo_12, Tramo_13, Tramo_14, Tramo_15, 
        Tramo_16, Tramo_17, Tramo_18, Tramo_19, Tramo_20, 
        Tramo_21, Tramo_22
    ]

    Recta_A = [ Ctrl_ON, 14,15,16,17,18,19 ]
    Recta_B = [ Ctrl_ON, 81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98 ]
    Recta_C = [ Ctrl_ON, 112,113,114,115,116,117,118,119 ]
    Recta_D = [ Ctrl_ON, 130,131,132,133,134,135,136,137 ]
    Recta_E = [ Ctrl_ON, 144,145,146,147,148,149 ]
    Recta_F = [ Ctrl_ON, 160,161,162,163,164,165,166,167,168 ]
    Recta_G = [ Ctrl_ON, 177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194 ]

    Rectas = [
        Recta_A, Recta_B, Recta_C, 
        Recta_D, Recta_E, Recta_F, 
        Recta_G
    ]
    
    # Si el control esta Ctrl_OFF, la función de dirección retorna Ok
    # si el control esta ON y coincide esta OK, sino False
    @staticmethod
    def direccion_ok(waypoint, dir):

        for t in CarControl.Tramos:
            if (waypoint in t):
                is_off = (CarControl.Ctrl_OFF in t)   
                dir_ok = (dir in t)
                if PRINT_LOG:
                   print(f"direccion_ok({waypoint},{dir})={t} esta la dir en el tramo? {dir_ok}")
                if (is_off):
                    return True
                return dir_ok

        return False


    @staticmethod
    def is_recta_B(waypoint):
        return (waypoint in CarControl.Recta_B)
    
    @staticmethod
    def is_recta_G(waypoint):
        return (waypoint in CarControl.Recta_G)
    

    # Si el control esta Ctrl_OFF, la funcion "esta en la recta" da falso
    # si el control esta ON y el waypoint esta en un recta "True"
    @staticmethod
    def esta_en_la_recta(waypoint):

        for r in CarControl.Rectas:
            is_off = (CarControl.Ctrl_OFF in r)
            if (is_off):
                continue
            if (waypoint in r):
                if PRINT_LOG:
                   print(f"esta_en_la_recta({waypoint})={r} esta en recta (True)")
                return True

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

def aux_is_counter_clockwise(params):

    is_reversed  = params['is_reversed'] # is clockwise (True) or counter clockwise (False).
    is_clockwise = is_reversed
    is_counter_clockwise = is_reversed

    return is_counter_clockwise

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

    # Waypoints
    closest_waypoints = params['closest_waypoints']
    wp_Cerca0 = closest_waypoints[0]
    wp_Cerca1 = closest_waypoints[1]


    REWARD_ZERO = 1e-3

    # Give a very low reward by default
    reward = 1e-3

    # Si Off track Retorna Zero
    if is_offtrack:
        return REWARD_ZERO

    # Si Counter Clockwise
    if aux_is_counter_clockwise(params):
        return REWARD_ZERO


    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0


    # Penalize reward if the car is steering too much
    #       En la recta tolerancia al angulo en rectas
    #                 - Mayor castigo y a su vez
    is_recta = CarControl.esta_en_la_recta(wp_Cerca1)
    ABS_STEERING_UMBRAL = 10  if is_recta else 15
    KKK_STEARING_PUNISH = 0.7 if is_recta else 0.8

    if abs_steering > ABS_STEERING_UMBRAL:
        reward *= KKK_STEARING_PUNISH


    # Penalize reward heading vs track is high
    # ABS_ANGLE_DIFF_UMBRAL = 10
    ABS_ANGLE_DIFF_UMBRAL = 8  if is_recta else 10

    angleDiffernce = aux_heading_vs_track_angle(params)

    if angleDiffernce > ABS_ANGLE_DIFF_UMBRAL:
        reward *= 0.7


    # Penalize reward si la direccion del auto (L, C, R) esta lejos del desado para el tramo
    # En este caso, solo en el tramo de Waypoints (62,63,64,65,66) y Left

    dir = CarControl.aux_side(params)

    if not CarControl.direccion_ok(wp_Cerca1, dir):
        reward *= 0.8

    
    # Penalizo velocidad Mínima en las Rectas (RECTAB)
    RECTAB_VEL_MIN = 1.4
    if CarControl.is_recta_B(wp_Cerca1):
        if speed < RECTAB_VEL_MIN:
            reward *= 0.8

    # Penalizo velocidad Mínima en las Rectas (RECTAG)
    RECTAG_VEL_MIN = 1.5
    if CarControl.is_recta_G(wp_Cerca1):
        if speed < RECTAG_VEL_MIN:
            reward *= 0.8


    # Speed y Progreso
    SPEED_UMBRAL = 3
    if speed < SPEED_UMBRAL:
        reward *= 0.8
    if progress == 100:    
        reward += 100

    return float(reward)

