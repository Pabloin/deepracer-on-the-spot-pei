#-----------[  DATA  ]------------------------------------

    # # sept 2023	Roger Super Raceway	60.17m	Clockwise  (2022_september_pro_cw)


LAP_LENGHT = 60.17
LAP_WIDTH  = 01.07

VALUE_MAX_ = 1e3
VALUE_ZERO = 1e-3
AJUSTE_K = 1


#-----------[ UTILS ]-------------------
class Util:

    #----------------------------------------------------------------------------------------------------
    # Distancia a la racing line
    # - (ww) Calcula las distancias entre 2 puntos de carrera más cercanos
    # - (cw) Distancias entre el coche y el punto de carrera más cercano 
    #                                 y el segundo más cercano
    # - (cl) Calcular la distancia entre el coche y la línea de carrera.
    #               (en el medio de los dos puntos mas cercanos de la rl)
    @staticmethod
    def distanciaRacingLine(auto, wCerca, wCerca_next):
        
        cl = abs(Util._distAB(auto[0],   wCerca_next[0], auto[1],   wCerca_next[1] ))
        cw = abs(Util._distAB(auto[0],   wCerca[0],      auto[1],   wCerca[1]      ))
        ww = abs(Util._distAB(wCerca[0], wCerca_next[0], wCerca[1], wCerca_next[1] ))
        
        try:
            distancia = abs(Util._diffWP(ww, cw) + Util._diffWP(ww, cl) + Util._diffWP(cw, cl))**0.5 / (2*ww)
            return distancia
        except:
            return cw

    #----------------------------------------------------------------------------------------------------
    # Indice de los 2 raicepoints más cercanos
    # - Calcular todas las distancias a los puntos de carrera y obtiene los dos más cercanos
    # Obtienr [x, y, velocidad, tiempo] óptimo para el índice más cercano y el segundo más cercano
    @staticmethod
    def racingPointsCercanos(wp, racingLine):

        dUno = []
        dDos = []

        for i in range(len(racingLine)):
            dist = Util._distAB(racingLine[i][0], wp[0],  racingLine[i][1], wp[1])
            dUno.append(dist)
            dDos.append(dist)

        cercaIdxUno = dUno.index(min(dUno))


        dDos[cercaIdxUno] = VALUE_MAX_

        cercaIdxDos = dDos.index(min(dDos))

        cercaUno = racingLine[cercaIdxUno]
        cercaDos = racingLine[cercaIdxDos]

        return [cercaUno, cercaDos]
    

    #----------------------------------------------------------------------------------------------------
    # Distancias entre los puntos A y B
    @staticmethod
    def _distAB(a1, a2, b1, b2):
        return abs(abs(a1-a2)**2 
                 + abs(b1-b2)**2)**0.5

    #----------------------------------------------------------------------------------------------------
    # Diferencia entre los waypoints W1 y W2
    @staticmethod
    def _diffWP(w1, w2):
        return 2*(w1**2)*(w2**2) - (w1**4)


class MyRacingLine:

    # sept 2023,Roger Super Raceway	60.17m	Clockwise  (2022_september_pro_cw)
    # Optimal racing line (x, y, velocidad)
    RACING_LINE = [
        [ 4.82610189, -3.96823104],
        [ 5.00873224, -3.73201441],
        [ 5.17819472, -3.48511455],
        [ 5.33809177, -3.23092152],
        [ 5.49177181, -2.97222687],
        [ 5.64198236, -2.71116968],
        [ 5.79159873, -2.44977126],
        [ 5.94065299, -2.1880516 ],
        [ 6.08916975, -1.92602629],
        [ 6.23717223, -1.66371036],
        [ 6.38468335, -1.40111748],
        [ 6.53172439, -1.13826094],
        [ 6.67830936, -0.87514979],
        [ 6.82445364, -0.61179331],
        [ 6.97017018, -0.34820001],
        [ 7.11547183, -0.08437781],
        [ 7.26036763,  0.17966714],
        [ 7.40486693,  0.44392969],
        [ 7.54321571,  0.71013029],
        [ 7.6648622 ,  0.98120937],
        [ 7.76517682,  1.25824658],
        [ 7.84551272,  1.54066069],
        [ 7.91061091,  1.82706174],
        [ 7.96602058,  2.11595058],
        [ 8.01537945,  2.40758338],
        [ 8.08092154,  2.69549287],
        [ 8.16439043,  2.97908589],
        [ 8.26459156,  3.25843915],
        [ 8.37868424,  3.53406525],
        [ 8.50236968,  3.80695928],
        [ 8.63035275,  4.07857309],
        [ 8.75960849,  4.34961828],
        [ 8.8771654 ,  4.62412968],
        [ 8.97169253,  4.90490668],
        [ 9.02198632,  5.19373826],
        [ 9.01245504,  5.48089943],
        [ 8.9407506 ,  5.75050498],
        [ 8.81438414,  5.99421966],
        [ 8.64306975,  6.21080369],
        [ 8.43567607,  6.40214253],
        [ 8.20005009,  6.57142274],
        [ 7.94372539,  6.72253483],
        [ 7.67593694,  6.86010504],
        [ 7.40431591,  6.99023809],
        [ 7.12882852,  7.11193519],
        [ 6.8494478 ,  7.22433874],
        [ 6.56629994,  7.32681041],
        [ 6.27964837,  7.41899963],
        [ 5.98969811,  7.50026989],
        [ 5.69673443,  7.57001328],
        [ 5.40139171,  7.61576057],
        [ 5.10797697,  7.62522186],
        [ 4.81985699,  7.59558474],
        [ 4.53893197,  7.52934164],
        [ 4.26635804,  7.42962187],
        [ 4.00372436,  7.2974402 ],
        [ 3.75529065,  7.13135295],
        [ 3.55083687,  6.93224583],
        [ 3.40332852,  6.71223449],
        [ 3.30892788,  6.4812232 ],
        [ 3.26059835,  6.24991592],
        [ 3.24776044,  6.02825059],
        [ 3.25766896,  5.81897532],
        [ 3.27971993,  5.61680279],
        [ 3.30111606,  5.34806064],
        [ 3.31233981,  5.06449046],
        [ 3.31222671,  4.77108113],
        [ 3.30135518,  4.4727438 ],
        [ 3.28068643,  4.17280567],
        [ 3.25055283,  3.8732276 ],
        [ 3.20864985,  3.57554677],
        [ 3.15066161,  3.28184781],
        [ 3.07382628,  2.99373572],
        [ 2.97700448,  2.71223326],
        [ 2.85886465,  2.43850562],
        [ 2.71773466,  2.17422808],
        [ 2.55246055,  1.92260152],
        [ 2.35602643,  1.69694159],
        [ 2.12415024,  1.5189978 ],
        [ 1.86413834,  1.40251029],
        [ 1.58741067,  1.34919498],
        [ 1.30381508,  1.35426673],
        [ 1.02060472,  1.40982002],
        [ 0.74250493,  1.5061489 ],
        [ 0.47137087,  1.63125815],
        [ 0.20552778,  1.77152598],
        [-0.06194752,  1.90987885],
        [-0.33091092,  2.04529026],
        [-0.60137235,  2.17771374],
        [-0.8731    ,  2.30757409],
        [-1.14374634,  2.4397224 ],
        [-1.41326421,  2.57415171],
        [-1.6817142 ,  2.71070259],
        [-1.9492226 ,  2.84909193],
        [-2.21595777,  2.98896921],
        [-2.48210654,  3.12996135],
        [-2.74785037,  3.27171758],
        [-3.01335299,  3.41392457],
        [-3.27906905,  3.55573051],
        [-3.54502978,  3.69707531],
        [-3.81122464,  3.83797799],
        [-4.07762829,  3.97848576],
        [-4.34421682,  4.1186434 ],
        [-4.6106425 ,  4.25910858],
        [-4.87689164,  4.3999076 ],
        [-5.14292882,  4.54110726],
        [-5.40870953,  4.68279147],
        [-5.67480877,  4.82387961],
        [-5.94160557,  4.96364331],
        [-6.20947022,  5.10134591],
        [-6.47979032,  5.21818837],
        [-6.75005698,  5.27752139],
        [-7.01183221,  5.26813093],
        [-7.25810007,  5.19373382],
        [-7.48498992,  5.06272091],
        [-7.69132253,  4.88490984],
        [-7.87773529,  4.66996654],
        [-8.04749787,  4.42907139],
        [-8.2061193 ,  4.17383438],
        [-8.36063141,  3.91530776],
        [-8.51165469,  3.65472751],
        [-8.65824461,  3.39162445],
        [-8.79912043,  3.12543941],
        [-8.91897018,  2.84957362],
        [-9.00127897,  2.56194483],
        [-9.03222727,  2.26737227],
        [-9.00448826,  1.97562982],
        [-8.91864381,  1.69708412],
        [-8.7810449 ,  1.43952174],
        [-8.60084017,  1.20708673],
        [-8.38817756,  1.00014034],
        [-8.15240352,  0.81620236],
        [-7.90160601,  0.65061873],
        [-7.64224768,  0.49760784],
        [-7.37932901,  0.35068478],
        [-7.11481762,  0.20664614],
        [-6.84991751,  0.0633303 ],
        [-6.60440479, -0.09140501],
        [-6.41502738, -0.27463859],
        [-6.29050988, -0.48462289],
        [-6.22691345, -0.71479913],
        [-6.21840783, -0.95961626],
        [-6.25933299, -1.21484472],
        [-6.34272651, -1.47698636],
        [-6.45834578, -1.74309065],
        [-6.59257102, -2.01113504],
        [-6.72943114, -2.27943347],
        [-6.86667372, -2.54753594],
        [-7.00504461, -2.81505698],
        [-7.14378957, -3.08238418],
        [-7.27860854, -3.34924698],
        [-7.36616834, -3.61927165],
        [-7.38655626, -3.88643979],
        [-7.33752599, -4.1414655 ],
        [-7.22554268, -4.37740047],
        [-7.05997289, -4.59024437],
        [-6.85178431, -4.77907731],
        [-6.6134797 , -4.94672545],
        [-6.3573215 , -5.09924293],
        [-6.0933249 , -5.24422741],
        [-5.82923603, -5.38904357],
        [-5.56510544, -5.53378391],
        [-5.30096149, -5.67850018],
        [-5.03683066, -5.82323861],
        [-4.77273989, -5.96805191],
        [-4.50872102, -6.11299552],
        [-4.2448479 , -6.25820462],
        [-3.98112104, -6.4036786 ],
        [-3.71754544, -6.54942614],
        [-3.45412701, -6.69545738],
        [-3.1908781 , -6.8417939 ],
        [-2.92786364, -6.98855093],
        [-2.6650803 , -7.13571939],
        [-2.40260899, -7.28343701],
        [-2.13833919, -7.42520984],
        [-1.86440917, -7.53470563],
        [-1.58224955, -7.59565737],
        [-1.29744552, -7.60360886],
        [-1.01519817, -7.56200843],
        [-0.73873548, -7.4784331 ],
        [-0.46907671, -7.3625927 ],
        [-0.20533151, -7.22484455],
        [ 0.05459723, -7.07481699],
        [ 0.31314829, -6.92033084],
        [ 0.57184487, -6.7660885 ],
        [ 0.83063158, -6.61199689],
        [ 1.08954749, -6.45812368],
        [ 1.34850204, -6.3043139 ],
        [ 1.60744798, -6.15049052],
        [ 1.8662694 , -5.99645822],
        [ 2.12490278, -5.84211124],
        [ 2.38335395, -5.68746024],
        [ 2.64165023, -5.53255122],
        [ 2.89981877, -5.37742962],
        [ 3.15783185, -5.22204938],
        [ 3.41568899, -5.06640887],
        [ 3.67331726, -4.91038845],
        [ 3.92881871, -4.75115207],
        [ 4.17579269, -4.58048694],
        [ 4.40899284, -4.39341369],
        [ 4.62531918, -4.18836481],
        [ 4.82610189, -3.96823104]
    ]

    #-----------[  RACING LINE - END  ]-------------------


RECTA_01     = 'RECTA_01'
RECTA_02     = 'RECTA_02'
RECTA_03     = 'RECTA_03'
RECTA_04     = 'RECTA_04'

RECTA_INI     = 'RECTA_INI'
RECTA_FIN     = 'RECTA_FIN'

CURVA_01_RR  = 'CURVA_01_RR'
CURVA_02_RR  = 'CURVA_02_RR'
CURVA_03_LL  = 'CURVA_03_LL'
CURVA_04_RR  = 'CURVA_04_RR'
CURVA_05_RR  = 'CURVA_05_RR'
CURVA_06_LL  = 'CURVA_06_LL'
CURVA_07_RR  = 'CURVA_07_RR'
CURVA_08_RR  = 'CURVA_08_RR'

PATH_01      = 'PATH_01'
PATH_02      = 'PATH_02'
PATH_03      = 'PATH_03'
PATH_04      = 'PATH_04'
PATH_05      = 'PATH_05'

class Track:

    # RogueRaceway  aka  2022_march_pro
    # PRO - Clockwise (76.76m) 
    Zones = [

        [RECTA_01        , 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22, RECTA_INI],
        [CURVA_01_RR     , 23,24,25,26,27,28],
        [RECTA_02        , 29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48],
        [CURVA_02_RR     , 49,50,51,52],

        [PATH_01         , 53,54,55,56,57,58,59,60],
        [CURVA_03_LL     , 61,62,63,64,65,66],
        
        [PATH_02         , 67,68,69,70,71,72,73],
        [CURVA_04_RR     , 74,75,76,77,78],
        
        [PATH_03         , 79,80,81,82,83,84,85,86,87,88],
        [CURVA_05_RR     , 89,90,91,92,93],

        [RECTA_03        , 94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120],
        [CURVA_06_LL     , 121,122,123,124,125,126],
        
        [PATH_04         , 127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144],
        [CURVA_07_RR     , 145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163],
        
        [PATH_05         , 164,165,166,167,168,169],
        [CURVA_08_RR     , 170,171,172,173,174,175,176,177,178,179,180],
        [RECTA_04        , 181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200, RECTA_FIN]

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
        zona = Track.Zones[0] 
        return (wp in zona and z in zona ) 
    

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
    def xSteeringCastigo(steering_angle, STEERING_VAL):
        steering = abs(steering_angle) 
        if steering > STEERING_VAL:
            return 0.8
        return 1
            

                    
#----------------------------------------
# Version z02
#
class MyDeepRacerClass:

    def rewardFunction_vZ02(self, params):
       
        #-----------[ INPUT PARAMETERS] -------------------

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
        track_length         = params['track_length']
        

        isLap_n1, isLap_n2, isLap_n3 = Track.isLap(track_length)

        
        #-----------[ Distancia a la Racing Line] -------------------

        racingLine = MyRacingLine.RACING_LINE

        cercaUno, cercaDos = Util.racingPointsCercanos([x, y], racingLine)

        dist = Util.distanciaRacingLine([x, y], cercaUno, cercaDos)

        REWARD = 1

        ## Recompensa por el waypoint ##
        wp_reward = max(1 - (dist/(track_width*0.5)), VALUE_ZERO)
        REWARD += wp_reward


        #-----------[ Stearing ] -------------------
        STEERING_THRESHOLD_ABS   =  15

        REWARD *= Track.xSteeringCastigo(steering_angle, STEERING_THRESHOLD_ABS)

        #-----[Velocidad]---------------------------------------------------------
        ## Le sumo el reward por menor gap
        
        # speed_deseada = cercaUno[2]
        # if Track.isRectaR3(closest_waypoints) or Track.isRectaR4(closest_waypoints):
        #     speed_deseada *= 1.15

        # REWARD *= Track.xSpeedCastigo(speed, speed_deseada)        

        ## Lo Castigo si el gap esta muy lejos de 4.0 hasta 3.1
        isRectaFin   = Track.isz(RECTA_FIN, closest_waypoints)
        if isRectaFin and isLap_n3:
            speed_deseada = 4.0
            REWARD *= Track.xSpeedCastigo(speed, speed_deseada)
            



        # #-----[Recta Veloz]---------------------------------------------------
        # # Recta veloz R3
        # if Track.isRecta(closest_waypoints):
        #     speed_deseada = 2.8
        #     REWARD *= Track.xSpeedPremio(speed, speed_deseada)
        
    
        # #-----[Recta Veloz]---------------------------------------------------
        # # Recta veloz R4
        # if Track.isRecta(closest_waypoints):
        #     speed_deseada = 3.4
        #     REWARD *= Track.xSpeedPremio(speed, speed_deseada)
        


        # reward += ( params["speed"] / 8 )
        
        ## Zero recompensa si off track ##
        if all_wheels_on_track == False:
            REWARD = VALUE_ZERO
            
        return float(REWARD)

#20230831 f01
#20230901 f01a
#20230901 f01b
myDR = MyDeepRacerClass()

def reward_function(params):
    return myDR.rewardFunction_vZ02(params)
    
    
    
