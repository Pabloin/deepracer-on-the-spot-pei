def reward_function(params):

    # Rogue Raceway  aka  2022_march_pro
    #              (76.76m) 

    # PRO - 
    #    OBJ CW -- Clockwise 
    #       Time TBS
    #       vuelta 1 - TBD   (0 off)
    #       vuelta 2 - TBD   (? off   zona 3) 
    

    # Enviado nn/nn/2023 por la WEB


    # Example of penalize steering, which helps mitigate zig-zag behaviors

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle

    track_length = params['track_length']
    
    LAP_LENGHT = 76.76
    LAP_WIDTH  = 01.07

    LAP_NUMBER_01 =                                    track_length <= LAP_LENGHT * 1
    LAP_NUMBER_02 = track_length >  LAP_LENGHT * 1 and track_length <= LAP_LENGHT * 2
    LAP_NUMBER_03 = track_length >  LAP_LENGHT * 2 and track_length <= LAP_LENGHT * 3

    dir_L  = 'LEFT'
    dir_C  = 'CENTER'
    dir_R  = 'RIGHT'

    Vel_01_MIN    = 'MIN'
    Vel_03_SLOW   = 'SLOW'
    Vel_05_MEDIO  = 'MEDIO'
    Vel_07_FAST   = 'FAST'
    Vel_10_MAX    = 'MAX'

    velz01_min    = []
    velz03_slow   = []    
    velz05_medio  = []
    velz07_fast   = []
    velz10_max    = []

    lst_L         = []
    lst_C         = []   
    lst_R         = []

    Zones       = [

        [dir_C, Vel_05_MEDIO, 255,254,253,252,251,250,249,248],
        [dir_L, Vel_03_SLOW,  247,246,245,244,243,242,241,240],
        [dir_L, Vel_03_SLOW,  239,238,237,236,235,234,233],
        [dir_L, Vel_05_MEDIO, 232,231,230,229,228,227,226],
        [dir_C, Vel_07_FAST,  225,224,223,222,221],
        [dir_C, Vel_05_MEDIO, 220,219,218,217,216,215],
        [dir_R, Vel_03_SLOW,  214,213,212,211,210,209,208,207,206,205,204,203,202],
        [dir_R, Vel_03_SLOW,  201,200,199,198,197,196,195],
        [dir_C, Vel_05_MEDIO, 194,193,192,191,190,189,188],
        [dir_R, Vel_05_MEDIO, 187,186,185,184,183,182,181,180,179,178,177],

        [dir_C, Vel_07_FAST,  176,175,174,173,172,171,170,169,168,167],
        [dir_R, Vel_10_MAX,   166,165,164,163,162,161,160],
        [dir_R, Vel_10_MAX,   159,158,157,156,155,154,153,152,151],
        [dir_R, Vel_07_FAST,  150,149,148,147,146,145,144,143,142],
        [dir_R, Vel_07_FAST,  141,140,139,138,137,136,135,134,133,132],
       
        [dir_C, Vel_05_MEDIO, 131,130,129,128,127,126,125,124],
        [dir_R, Vel_03_SLOW,  123,122,121,120,119,118,117],
        [dir_R, Vel_01_MIN,   116,115,114,113,112,111],
        [dir_R, Vel_01_MIN,   110,109,108,107,106,105,104],

        [dir_C, Vel_03_SLOW,  103,102,101,100],
        [dir_L, Vel_01_MIN,   99,98,97,96,95,94],

        [dir_L, Vel_03_SLOW,  93,92,91,90,89,88,87,86],
        [dir_L, Vel_03_SLOW,  85,84,83,82,81,80,79,78],
        [dir_L, Vel_01_MIN,   77,76,75,74,73,72],

        [dir_C, Vel_03_SLOW,  71,70,69,68],
        [dir_R, Vel_01_MIN,   67,66,65,64,63],

        [dir_R, Vel_01_MIN,   62,61,60,59,58],
        [dir_R, Vel_03_SLOW,  57,56,55,54,53,52,51],

        [dir_R, Vel_05_MEDIO, 50,49,48,47,46,45],
        [dir_R, Vel_03_SLOW,  39,38,37,36,39],
        [dir_C, Vel_05_MEDIO, 35,34,33,32],

        [dir_R, Vel_05_MEDIO, 31,30,29,28],
        [dir_R, Vel_05_MEDIO, 27,26,25,24,23],
        [dir_R, Vel_05_MEDIO, 22,21,20,19,18],
        [dir_R, Vel_07_FAST,  17,16,15,14,13,12,11,10],
        [dir_R, Vel_07_FAST,  9,8,7,6,5],
        [dir_R, Vel_07_FAST,  4,3,2,1]

    ]

    for z in Zones:

        if   Vel_01_MIN   in z:
             velz01_min   = velz01_min + z

        elif Vel_03_SLOW  in z:
             velz03_slow  = velz03_slow + z  

        elif Vel_05_MEDIO in z:
             velz05_medio = velz05_medio + z 

        elif Vel_07_FAST  in z:
             velz07_fast  = velz07_fast + z 

        elif Vel_10_MAX   in z:
             velz10_max   = velz10_max + z 


        if   dir_L in z:
             lst_L =  lst_L + z

        elif dir_C in z:
             lst_C =  lst_C + z 

        elif dir_R in z:
             lst_R =  lst_R + z

       



    reward = 50
   
    VELOCIDAD_MAX_VAL    = 1.70
    VELOCIDAD_FAST       = 1.40
    VELOCIDAD_MEDIUM     = 1.20
    VELOCIDAD_SLOW       = 1.05
    VELOCIDAD_MIN        = 0.80

    center_variance = params["distance_from_center"] / params["track_width"]

    if  params["all_wheels_on_track"]:
        reward += 10
    else:
        reward -= 10



    if   params["closest_waypoints"][1] in lst_L  and     params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in lst_R  and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in lst_C  and     center_variance < 0.4:
        reward += 10
    else:
        reward -= 10



    if params["closest_waypoints"][1] in velz10_max:

        if params["speed"] >= VELOCIDAD_MAX_VAL:
            reward += 10
        else:
            reward -= 10

    if params["closest_waypoints"][1] in velz07_fast:

        if params["speed"] >= VELOCIDAD_FAST   and params["speed"] < VELOCIDAD_MAX_VAL:
            reward += 10
        else:
            reward -= 10

    elif params["closest_waypoints"][1] in velz05_medio:

        if params["speed"] >= VELOCIDAD_MEDIUM and params["speed"] < VELOCIDAD_FAST:
            reward += 10
        else:
            reward -= 10

    elif params["closest_waypoints"][1] in velz03_slow:

        if params["speed"] >= VELOCIDAD_SLOW   and params["speed"] < VELOCIDAD_SLOW:
            reward += 10
        else:
            reward -= 10

    elif params["closest_waypoints"][1] in velz01_min:

        if params["speed"] >= VELOCIDAD_MIN   and params["speed"] < VELOCIDAD_MEDIUM:
            reward += 10
        else:
            reward -= 10


    return float(reward)


