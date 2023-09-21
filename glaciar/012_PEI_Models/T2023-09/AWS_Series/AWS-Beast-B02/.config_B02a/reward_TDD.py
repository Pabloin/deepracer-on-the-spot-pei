LAP_LENGHT = 60.17
LAP_WIDTH  = 01.07

VALUE_MAX_ = 1e3
VALUE_ZERO = 1e-3
AJUSTE_K = 1

MODE_DEBUG = True

RECTA_01           = 'RECTA_01'
RECTA_02           = 'RECTA_02'
RECTA_03           = 'RECTA_03'
RECTA_04           = 'RECTA_04'

RECTA_INI          = 'RECTA_INI'
RECTA_FIN          = 'RECTA_FIN'

CURVA_01_RR        = 'CURVA_01_RR'
CURVA_02_RR        = 'CURVA_02_RR'
CURVA_03_LL        = 'CURVA_03_LL'
CURVA_03_LL_ZONA   = 'CURVA_03_LL_ZONA'
CURVA_04_RR        = 'CURVA_04_RR'
CURVA_05_RR        = 'CURVA_05_RR'
CURVA_06_LL        = 'CURVA_06_LL'
CURVA_06_LL_ZONA   = 'CURVA_06_LL_ZONA'
CURVA_07_RR        = 'CURVA_07_RR'
CURVA_08_RR        = 'CURVA_08_RR'

PATH_01            = 'PATH_01'
PATH_02            = 'PATH_02'
PATH_03            = 'PATH_03'
PATH_04            = 'PATH_04'
PATH_05            = 'PATH_05'

class Track:

    # RogueRaceway  aka  2022_march_pro
    # PRO - Clockwise (76.76m) 
    Zones = [

        [RECTA_01           , 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22, RECTA_INI],
        [CURVA_01_RR        , 23,24,25,26,27,28],
        [RECTA_02           , 29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48],
        [CURVA_02_RR        , 49,50,51,52],

        [PATH_01            , 53,54,55,56,57,58,59,60],
        [CURVA_03_LL        , 61,62,63,64,65,66],
        
        [CURVA_03_LL_ZONA   , 58,59,60,61,62,63,64,65,66,67,68,69],


        [PATH_02            , 67,68,69,70,71,72,73],
        [CURVA_04_RR        , 74,75,76,77,78],
        
        [PATH_03            , 79,80,81,82,83,84,85,86,87,88],
        [CURVA_05_RR        , 89,90,91,92,93],

        [RECTA_03           , 94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120],
        [CURVA_06_LL        , 121,122,123,124,125,126],
        

        [CURVA_06_LL_ZONA   , 117,118,119,120,  121,122,123,124,125,126,  127,128],


        [PATH_04            , 127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144],
        [CURVA_07_RR        , 145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163],
        
        [PATH_05            , 164,165,166,167,168,169],
        [CURVA_08_RR        , 170,171,172,173,174,175,176,177,178,179,180],
        [RECTA_04           , 181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200, RECTA_FIN]

    ]



    #----------------------------------------------------------------------------------------------------
    # Dice si es Lap 1, dos o tres
    @staticmethod
    def isLap(track_length):

        isLap_n1 =                                    track_length <= LAP_LENGHT * 1
        isLap_n2 = track_length >  LAP_LENGHT * 1 and track_length <= LAP_LENGHT * 2
        isLap_n3 = track_length >  LAP_LENGHT * 2 and track_length <= LAP_LENGHT * 3

        return [isLap_n1, isLap_n2, isLap_n3]
    
    #----------------------------------------------------------------------------------------------------
    # Dice la zona
    @staticmethod
    def isz(z, wp):
        isInZone = False
        for zone in Track.Zones:
            if (wp in zone and z in zone):
                return True
        return isInZone


    #----------------------------------------------------------------------------------------------------
    # Dice si es una Recta
    @staticmethod
    def isRecta(wp):
        return (Track.isz(RECTA_01, wp) or 
                Track.isz(RECTA_02, wp) or 
                Track.isz(RECTA_03, wp) or 
                Track.isz(RECTA_04, wp))

    #----------------------------------------------------------------------------------------------------
    # Dice si es una Curva Left
    @staticmethod
    def isCurvaLeft(wp):
        return (Track.isz(CURVA_03_LL, wp) or 
                Track.isz(CURVA_06_LL, wp))

    #----------------------------------------------------------------------------------------------------
    # Dice si es una Curva Right
    @staticmethod
    def isCurvaRight(wp):
        return (Track.isz(CURVA_01_RR, wp) or 
                Track.isz(CURVA_02_RR, wp) or 
                Track.isz(CURVA_04_RR, wp) or 
                Track.isz(CURVA_05_RR, wp) or 
                Track.isz(CURVA_07_RR, wp) or 
                Track.isz(CURVA_08_RR, wp))

    #----------------------------------------------------------------------------------------------------
    # Speed Castigo
    @staticmethod
    def xSpeedCastigo(speed, speed_deseada):

        gap = abs(speed_deseada-speed)

        gapVel = [
            #min  max   rew
            [ 0.0,  0.1,  1.00 ],
            [ 0.1,  0.2,  1.00 ],
            [ 0.2,  0.3,  0.90 ],
            [ 0.3,  0.4,  0.80 ],
            [ 0.4,  0.5,  0.70 ],
            [ 0.5,  0.6,  0.70 ],
            [ 0.6,  0.7,  0.60 ],
            [ 0.7,  0.8,  0.60 ],
            [ 0.8,  0.9,  0.50 ],
            [ 0.9,  1.0,  0.50 ],
            [ 1.0,  1.1,  0.40 ],
            [ 1.1,  1.2,  0.40 ],
            [ 1.2,  1.3,  0.30 ],
            [ 1.3,  1.4,  0.30 ],
            [ 1.4,  1.5,  0.20 ],
            [ 1.5,  1.6,  0.20 ],
            [ 1.6,  1.9,  0.10 ],
            [ 2.1,  4.0,  0.00 ],
        ]        

        for e in gapVel:
            if  gap  >= e[0] and gap  < e[1]:
                print(" xSpeedCastigo(", speed, ",", speed_deseada, "): gap=", gap, " -> [", e[0], ",", e[1], ",", e[2], "]" )
                return e[2]

        return 1


    #----------------------------------------------------------------------------------------------------
    # Speed Premio
    @staticmethod
    def xSpeedPremio(speed, speed_deseada):

        if speed  >= speed_deseada:
            return 1

        gap = abs(speed_deseada-speed)

        gapVel = [
            #min  max   rew
            [ 0.0,  0.1,  1.60 ],
            [ 0.1,  0.2,  1.57 ],
            [ 0.2,  0.3,  1.55 ],
            [ 0.3,  0.4,  1.54 ],
            [ 0.4,  0.5,  1.50 ],
            [ 0.5,  0.6,  1.46 ],
            [ 0.6,  0.7,  1.42 ],
            [ 0.7,  0.8,  1.40 ],
            [ 0.8,  0.9,  1.36 ],
            [ 0.9,  1.0,  1.32 ],
            [ 1.0,  1.1,  1.28 ],
            [ 1.1,  1.2,  1.34 ],
            [ 1.2,  1.3,  1.20 ],
            [ 1.3,  1.4,  1.16 ],
            [ 1.4,  1.5,  1.12 ],
            [ 1.5,  1.6,  1.08 ],
            [ 1.6,  1.9,  1.04 ],
            [ 2.1,  4.0,  1.00 ],
        ]        

        for e in gapVel:
            if  gap  >= e[0] and gap  < e[1]:
                return e[2]

        return 1

    #----------------------------------------------------------------------------------------------------
    # Steering Castigo
    @staticmethod
    def xSteeringCastigo(steering_angle, STEERING_VAL, castigo=0.8):
        steering = abs(steering_angle) 
        if steering > STEERING_VAL:
            return castigo
        return 1
            

    #----------------------------------------------------------------------------------------------------
    # Direction de la Pista en Grados
    # - Calculate la direccion de la pista en grados (atan2)
    # - the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    # ... Podría calcular los xy para la direccion de la racing line ... 
    @staticmethod
    def _direccionPista(params):
       
        waypoints         = params['waypoints']
        closest_waypoints = params['closest_waypoints']

        wpNext = waypoints[closest_waypoints[1]]
        wpPrev = waypoints[closest_waypoints[0]]

        dirPista = math.degrees(math.atan2(wpNext[1] - wpPrev[1], 
                                           wpNext[0] - wpPrev[0]))

        return dirPista

    #----------------------------------------------------------------------------------------------------
    # Castigo por Heading vs DirPista
    @staticmethod
    def xHeadingCastigo(params, DIRECCION_ABS_VAL, castigo=0.5):
       
        heading = params['heading']

        dirPista = Track._direccionPista(params) 

        dirDiff = abs(dirPista - heading)
        if dirDiff > DIRECCION_ABS_VAL:
            return castigo


        #-------------------------------------------------------------
        if MODE_DEBUG:
            print("   dirPista: ", dirPista,  " - dirDiff: ", dirDiff, " - heading: ", heading ) 
        

        return 1
    


print('Hola')


# closest_waypoints: [1, 2]
# closest_waypoints[1]: 2
# closest_waypoints[0]: 1
# closest_waypoints: 1 2


# x: 4.5960888763624235 y: -4.3378093609562995    wpNext:  4.429752826690674 -4.417214512825012  - wpPrev:  4.654623508453369 -4.217042446136475  - speed:  1.25
# steering_angle:  30.0 heading:  -125.8884993664113 distance_from_center:  0.05128566786655362
# curva3 False curva6 False progress:  0.7063766453562026
# OTRA: x: 4.5960888763624235 y: -4.3378093609562995    wpNext:  4.429752826690674 -4.417214512825012  - wpPrev:  4.654623508453369 -4.217042446136475  - speed:  1.25
# OTRA: steering_angle:  30.0 heading:  -125.8884993664113 distance_from_center:  0.05128566786655362 progress:  0.7063766453562026
# SIM_TRACE_LOG:0,7,4.5961,-4.3378,-125.8885,30.00,1.25,[30.0, 1.25],1.0000,False,True,0.7064,1,60.18,42.173,in_progress,0.00


#SIM_TRACE_LOG:0,1,4.7634,-4.0986,-132.5784,-0.80,2.46,[-0.7983805874334244, 2.455950601998581],0.0000,False,True,0.2331,
# 
# 0,60.18,38.842,prepare,0.00

# wpNext = waypoints[closest_waypoints[1]]
# wpPrev = waypoints[closest_waypoints[0]]

closest_waypoints = [1, 2]

wpNext = [4.429752826690674, -4.417214512825012]    
wpPrev = [4.654623508453369, -4.217042446136475]    

# Mar recompensa en Cruva Tres y Seis
isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, wpNext)

isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, wpNext)
print("isZonaCurvaTres(", CURVA_03_LL_ZONA, ",", wpNext, ") = ", isZonaCurvaTres )


wpNext=12
isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, wpNext)
print("isZonaCurvaTres(", CURVA_03_LL_ZONA, ",", wpNext, ") = ", isZonaCurvaTres )


wpNext=61
isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, wpNext)
print("isZonaCurvaTres(", CURVA_03_LL_ZONA, ",", wpNext, ") = ", isZonaCurvaTres )


isZonaCurvaSeis   = Track.isz(CURVA_06_LL_ZONA, wpNext)


# curva3 False curva6 False







