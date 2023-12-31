#-----------[  DATA  ]------------------------------------

    # Rogue Raceway  aka  2022_march_pro
    # PRO - Clockwise (76.76m) 


LAP_LENGHT = 76.76
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

    # Rogue Raceway  aka  2022_march_pro
    # Optimal racing line (x, y, velocidad)
    RACING_LINE = [
        [0.89414, -0.39536, 4.0],
        [0.64688, -0.37173, 4.0],
        [0.40178, -0.34807, 4.0],
        [0.15899, -0.3244, 4.0],
        [-0.08085, -0.30068, 4.0],
        [-0.33696, -0.27614, 4.0],
        [-0.60425, -0.2521, 4.0],
        [-0.88142, -0.22976, 4.0],
        [-1.16535, -0.21055, 3.77642],
        [-1.4528, -0.19593, 3.38335],
        [-1.74099, -0.18734, 3.00667],
        [-2.02764, -0.18634, 2.71977],
        [-2.31085, -0.19447, 2.37626],
        [-2.58891, -0.21327, 2.09323],
        [-2.85995, -0.24465, 1.82489],
        [-3.12188, -0.29051, 1.82489],
        [-3.37213, -0.35305, 1.6954],
        [-3.6081, -0.43375, 1.4966],
        [-3.82552, -0.53519, 1.4966],
        [-4.01928, -0.65912, 1.41418],
        [-4.18215, -0.8066, 1.41418],
        [-4.31712, -0.97099, 1.41418],
        [-4.41757, -1.15182, 1.41418],
        [-4.47379, -1.34671, 1.41418],
        [-4.48841, -1.54838, 1.41418],
        [-4.45179, -1.75013, 1.53855],
        [-4.37043, -1.94434, 1.70123],
        [-4.25094, -2.12681, 1.8563],
        [-4.09777, -2.29474, 2.02148],
        [-3.9147, -2.44609, 2.20886],
        [-3.70544, -2.57959, 2.42698],
        [-3.47382, -2.69482, 2.68113],
        [-3.22375, -2.79212, 2.97976],
        [-2.95903, -2.87265, 3.31401],
        [-2.68301, -2.93796, 3.68444],
        [-2.39858, -2.9898, 4.0],
        [-2.10831, -3.03028, 4.0],
        [-1.81414, -3.06126, 4.0],
        [-1.51749, -3.08428, 4.0],
        [-1.21933, -3.10058, 4.0],
        [-0.92031, -3.11128, 4.0],
        [-0.6208, -3.11706, 4.0],
        [-0.32102, -3.11848, 4.0],
        [-0.02111, -3.11612, 4.0],
        [0.27888, -3.11051, 4.0],
        [0.5789, -3.10214, 4.0],
        [0.87893, -3.09135, 3.3736],
        [1.17897, -3.07819, 2.93707],
        [1.47901, -3.06256, 2.57873],
        [1.77282, -3.05192, 2.29925],
        [2.06226, -3.04989, 2.05651],
        [2.34501, -3.06024, 1.82661],
        [2.61815, -3.08683, 1.60807],
        [2.87851, -3.13263, 1.39627],
        [3.12234, -3.20017, 1.39627],
        [3.34565, -3.29081, 1.39627],
        [3.54401, -3.40513, 1.39627],
        [3.71193, -3.5432, 1.39627],
        [3.84212, -3.7043, 1.39627],
        [3.92369, -3.88612, 1.44783],
        [3.9605, -4.07996, 1.57212],
        [3.95828, -4.28005, 1.58502],
        [3.91929, -4.48293, 1.58502],
        [3.83426, -4.68448, 1.75683],
        [3.70692, -4.87889, 1.96263],
        [3.54305, -5.06092, 2.20045],
        [3.35018, -5.22685, 2.48151],
        [3.13597, -5.37566, 2.71722],
        [2.90558, -5.50732, 2.94489],
        [2.66288, -5.62252, 3.16655],
        [2.41065, -5.7223, 3.38581],
        [2.15095, -5.8078, 3.60508],
        [1.88533, -5.88015, 3.81976],
        [1.61495, -5.94038, 4.0],
        [1.34073, -5.98937, 4.0],
        [1.06336, -6.0278, 4.0],
        [0.78346, -6.05631, 4.0],
        [0.50155, -6.07544, 4.0],
        [0.2181, -6.0857, 4.0],
        [-0.06647, -6.08758, 4.0],
        [-0.35177, -6.08154, 4.0],
        [-0.63749, -6.06806, 4.0],
        [-0.92331, -6.04757, 4.0],
        [-1.20898, -6.02052, 4.0],
        [-1.49429, -5.98732, 4.0],
        [-1.77905, -5.94836, 4.0],
        [-2.06311, -5.90405, 4.0],
        [-2.34634, -5.85471, 4.0],
        [-2.62859, -5.80046, 4.0],
        [-2.90968, -5.74123, 3.98063],
        [-3.1893, -5.67657, 3.41641],
        [-3.467, -5.60581, 3.03678],
        [-3.74221, -5.52812, 2.64939],
        [-4.01413, -5.44234, 2.64939],
        [-4.28163, -5.34692, 2.64939],
        [-4.54342, -5.2403, 2.64939],
        [-4.79687, -5.11901, 2.64939],
        [-5.03908, -4.97988, 2.64939],
        [-5.26523, -4.81865, 3.22465],
        [-5.47953, -4.64352, 3.38311],
        [-5.6824, -4.45649, 3.56487],
        [-5.87447, -4.25939, 3.58067],
        [-6.05563, -4.05308, 3.47638],
        [-6.22573, -3.83833, 3.17252],
        [-6.38463, -3.6158, 2.63526],
        [-6.53218, -3.38611, 2.50256],
        [-6.66792, -3.14961, 2.50256],
        [-6.79096, -2.90652, 2.50256],
        [-6.90025, -2.65704, 2.50256],
        [-6.99266, -2.40077, 2.50256],
        [-7.05986, -2.13675, 2.50256],
        [-7.09834, -1.86723, 2.74727],
        [-7.1127, -1.59531, 3.05033],
        [-7.10737, -1.32268, 3.31884],
        [-7.08533, -1.05023, 3.58546],
        [-7.04889, -0.77852, 3.85987],
        [-6.99998, -0.50788, 4.0],
        [-6.94025, -0.23853, 4.0],
        [-6.87102, 0.02942, 4.0],
        [-6.79312, 0.29586, 4.0],
        [-6.70668, 0.56057, 4.0],
        [-6.61151, 0.82323, 4.0],
        [-6.50602, 1.083, 4.0],
        [-6.39157, 1.33978, 4.0],
        [-6.2693, 1.59357, 4.0],
        [-6.13995, 1.84433, 4.0],
        [-6.00395, 2.09191, 4.0],
        [-5.86157, 2.33616, 4.0],
        [-5.71313, 2.57691, 4.0],
        [-5.55872, 2.81388, 4.0],
        [-5.39845, 3.04677, 4.0],
        [-5.23247, 3.2753, 4.0],
        [-5.06112, 3.49927, 4.0],
        [-4.88482, 3.7186, 4.0],
        [-4.70401, 3.93326, 4.0],
        [-4.51908, 4.14318, 3.84124],
        [-4.33005, 4.34786, 3.51661],
        [-4.13697, 4.54675, 3.02412],
        [-3.93978, 4.739, 2.66031],
        [-3.7383, 4.92335, 2.33492],
        [-3.53231, 5.09816, 2.05308],
        [-3.32162, 5.26127, 1.81038],
        [-3.10628, 5.41051, 1.59648],
        [-2.88605, 5.54136, 1.45182],
        [-2.6615, 5.64927, 1.3985],
        [-2.43398, 5.72897, 1.3985],
        [-2.20615, 5.77472, 1.3985],
        [-1.98262, 5.7806, 1.3985],
        [-1.77109, 5.74065, 1.3985],
        [-1.58206, 5.65272, 1.3985],
        [-1.42497, 5.52121, 1.52],
        [-1.29991, 5.3581, 1.72441],
        [-1.20291, 5.17255, 1.74363],
        [-1.13714, 4.96623, 1.98919],
        [-1.09893, 4.74477, 2.23174],
        [-1.08557, 4.51197, 2.32513],
        [-1.09519, 4.27089, 2.00717],
        [-1.12541, 4.02526, 1.73658],
        [-1.17281, 3.78049, 1.53412],
        [-1.20459, 3.54218, 1.53412],
        [-1.21672, 3.30819, 1.53412],
        [-1.20442, 3.08019, 1.53412],
        [-1.16167, 2.86076, 1.53412],
        [-1.08036, 2.6542, 1.53412],
        [-0.95003, 2.46816, 1.90267],
        [-0.78648, 2.29911, 2.09821],
        [-0.59368, 2.14728, 2.30516],
        [-0.37486, 2.013, 2.57475],
        [-0.13402, 1.89586, 2.84012],
        [0.1254, 1.7955, 2.85245],
        [0.40015, 1.71161, 2.67539],
        [0.68795, 1.64599, 2.50151],
        [0.98368, 1.60127, 2.35269],
        [1.28044, 1.57906, 2.22715],
        [1.57306, 1.581, 2.11359],
        [1.85715, 1.60788, 2.00111],
        [2.12828, 1.66035, 1.88076],
        [2.38202, 1.7383, 1.67353],
        [2.61453, 1.84045, 1.50169],
        [2.82285, 1.96463, 1.33475],
        [3.00476, 2.10835, 1.33475],
        [3.15823, 2.26918, 1.33475],
        [3.28092, 2.44489, 1.33475],
        [3.36626, 2.63432, 1.33475],
        [3.40631, 2.8347, 1.33475],
        [3.38801, 3.04073, 1.65082],
        [3.32917, 3.24596, 1.86936],
        [3.23558, 3.44818, 2.17828],
        [3.11349, 3.6464, 2.36174],
        [2.97023, 3.84077, 2.10549],
        [2.81504, 4.03265, 1.84683],
        [2.66661, 4.23345, 1.63769],
        [2.53567, 4.4365, 1.45699],
        [2.42648, 4.64142, 1.3],
        [2.34209, 4.84737, 1.3],
        [2.28569, 5.05315, 1.3],
        [2.26197, 5.25687, 1.3],
        [2.27598, 5.45552, 1.3],
        [2.33458, 5.64402, 1.3],
        [2.44812, 5.8119, 1.51277],
        [2.60304, 5.9568, 1.69194],
        [2.79249, 6.07653, 1.88655],
        [3.01043, 6.1696, 2.09102],
        [3.25074, 6.23514, 2.29773],
        [3.50684, 6.27317, 2.52048],
        [3.77212, 6.28525, 2.67103],
        [4.04126, 6.27257, 2.79701],
        [4.3099, 6.2368, 2.92513],
        [4.5749, 6.18016, 2.81317],
        [4.83421, 6.10481, 2.59576],
        [5.08642, 6.01236, 2.35382],
        [5.33058, 5.90423, 2.35382],
        [5.5658, 5.78119, 2.35382],
        [5.7904, 5.64262, 2.35382],
        [6.00173, 5.48694, 2.35382],
        [6.19648, 5.31234, 2.35382],
        [6.36964, 5.1162, 2.59962],
        [6.52396, 4.9034, 2.80252],
        [6.66113, 4.67688, 2.98489],
        [6.78229, 4.43883, 3.19188],
        [6.88863, 4.19131, 3.30514],
        [6.98037, 3.93577, 3.40382],
        [7.05761, 3.67372, 3.37574],
        [7.12026, 3.40675, 3.26509],
        [7.16804, 3.13651, 3.10028],
        [7.20059, 2.86469, 2.89623],
        [7.21779, 2.59296, 2.63767],
        [7.21973, 2.32276, 2.33874],
        [7.20606, 2.05542, 2.33874],
        [7.17627, 1.79228, 2.33874],
        [7.12933, 1.53486, 2.33874],
        [7.0637, 1.28501, 2.33874],
        [6.97681, 1.04543, 2.2688],
        [6.86472, 0.82046, 2.2688],
        [6.73307, 0.60867, 2.2688],
        [6.58215, 0.41132, 2.2688],
        [6.41002, 0.23187, 2.2688],
        [6.21953, 0.06985, 2.2688],
        [6.00834, -0.06975, 2.47633],
        [5.78057, -0.18872, 2.67429],
        [5.53909, -0.28852, 2.92049],
        [5.28645, -0.37101, 3.11673],
        [5.02429, -0.43725, 3.34631],
        [4.75412, -0.48847, 3.61387],
        [4.47736, -0.52605, 3.92457],
        [4.19534, -0.55147, 4.0],
        [3.90932, -0.56626, 4.0],
        [3.62055, -0.57194, 4.0],
        [3.3303, -0.5698, 4.0],
        [3.04007, -0.5613, 4.0],
        [2.75154, -0.54779, 4.0],
        [2.4667, -0.53044, 4.0],
        [2.18764, -0.51035, 4.0],
        [1.91598, -0.48853, 4.0],
        [1.65221, -0.46573, 4.0],
        [1.39539, -0.44245, 4.0],
        [1.14351, -0.41894, 4.0],
    ]

    #-----------[  RACING LINE - END  ]-------------------



class MyDrTrack:

    # RogueRaceway  aka  2022_march_pro
    # PRO - Clockwise (76.76m) 

    Zones = [

        # 0 (Ri)
        [255,254,253,252,251,250,249,248],
        [247,246,245,244,243,242,241,240],

        # 2
        [239,238,237,236,235,234,233],
        [232,231,230,229,228,227,226],

        #4 (R2)
        [225,224,223,222,221],
        [220,219,218,217,216,215],
        [214,213,212,211,210,209,208,207,206,205,204,203,202],

        #7
        [201,200,199,198,197,196,195],
        [194,193,192,191,190,189,188],
        
        #9 (R3)
        [187,186,185,184,183,182,181,180,179,178,177],
        [176,175,174,173,172,171,170,169,168,167],
        [166,165,164,163,162,161,160],

        #12
        [159,158,157,156,155,154,153,152,151],
        [150,149,148,147,146,145,144,143,142],

        #14 (R4)
        [141,140,139,138,137,136,135,134,133,132],
        [131,130,129,128,127,126,125,124],
        [123,122,121,120,119,118,117],

        # 17
        [116,115,114,113,112,111],
        [110,109,108,107,106,105,104],
        [103,102,101,100],

        # 20
        [99,98,97,96,95,94],
        [93,92,91,90,89,88,87,86],
        [85,84,83,82,81,80,79,78],
        [77,76,75,74,73,72],
        [71,70,69,68],

        # 25
        [67,66,65,64,63],
        [62,61,60,59,58],
        [57,56,55,54,53,52,51],
        [50,49,48,47,46,45],
        [39,38,37,36,39],

        # 30
        [35,34,33,32],
        [31,30,29,28],
        [27,26,25,24,23],
        [22,21,20,19,18],

        # 35 (Rf)
        [17,16,15,14,13,12,11,10],
        [9,8,7,6,5],
        [4,3,2,1]
        # 36

    ]

    Zones_recta_R3 = [180, 160]
    Zones_recta_R4 = [144, 116]

    @staticmethod
    def isRectaVelozR3(wp):
        return MyDrTrack.isRectaVeloz(wp, MyDrTrack.Zones_recta_R3)

    @staticmethod
    def isRectaVelozR4(wp):
        return MyDrTrack.isRectaVeloz(wp, MyDrTrack.Zones_recta_R4)

    @staticmethod
    def isRectaVeloz(wp, recta):
        return (wp[0] >= recta[0] and wp[0] <= recta[1])
    
    #----------------------------------------------------------------------------------------------------
    # Dice si es Lap 1, dos o tres
    @staticmethod
    def isLap(track_length):

        isLap_n1 =                                    track_length <= LAP_LENGHT * 1
        isLap_n2 = track_length >  LAP_LENGHT * 1 and track_length <= LAP_LENGHT * 2
        isLap_n3 = track_length >  LAP_LENGHT * 2 and track_length <= LAP_LENGHT * 3

        return [isLap_n1, isLap_n2, isLap_n3]
    
    #----------------------------------------------------------------------------------------------------
    # Dice si es Recta Final
    @staticmethod
    def isRectaFin(wp):
        recta = MyDrTrack.Zones[34] + MyDrTrack.Zones[35] + MyDrTrack.Zones[36]
        return (wp in recta)
    
    #----------------------------------------------------------------------------------------------------
    # Dice si es Recta Inicial
    @staticmethod
    def isRectaIni(wp):
        recta = MyDrTrack.Zones[0] + MyDrTrack.Zones[1] 
        return (wp in recta) 

    #----------------------------------------------------------------------------------------------------
    # Dice si es Recta Dos
    @staticmethod
    def isRecta2(wp):
        recta = MyDrTrack.Zones[4] + MyDrTrack.Zones[5] + MyDrTrack.Zones[6] 
        return (wp in recta) 

    #----------------------------------------------------------------------------------------------------
    # Dice si es Recta Tres
    @staticmethod
    def isRecta3(wp):
        recta = MyDrTrack.Zones[9] + MyDrTrack.Zones[10] + MyDrTrack.Zones[11] 
        return (wp in recta)
    
    #----------------------------------------------------------------------------------------------------
    # Dice si es Recta Cuatro.
    @staticmethod
    def isRecta4(wp):
        recta = MyDrTrack.Zones[14] + MyDrTrack.Zones[15] + MyDrTrack.Zones[16] 
        return (wp in recta)
    
    #----------------------------------------------------------------------------------------------------
    # Dice si es Curva 1 Left
    @staticmethod
    def isCurva1L(wp):
        curva = MyDrTrack.Zones[2] + MyDrTrack.Zones[3] 
        return (wp in curva) 


    #----------------------------------------------------------------------------------------------------
    # Dice si es Curva 2 Right
    @staticmethod
    def isCurva2R(wp):
        curva = MyDrTrack.Zones[7] + MyDrTrack.Zones[8] + MyDrTrack.Zones[16] 
        return (wp in curva) 
    

    #----------------------------------------------------------------------------------------------------
    # Dice si es Curva 3 Right
    @staticmethod
    def isCurva3R(wp):
        curva = MyDrTrack.Zones[17] + MyDrTrack.Zones[18] + MyDrTrack.Zones[19] 
        return (wp in curva) 

    #----------------------------------------------------------------------------------------------------
    # Dice si es Curva 4 Left
    @staticmethod
    def isCurva4L(wp):
        curva = MyDrTrack.Zones[20] + MyDrTrack.Zones[21] 
        return (wp in curva)
    
    #----------------------------------------------------------------------------------------------------
    # Dice si es Curva 5 Left
    @staticmethod
    def isCurva5L(wp):
        curva = MyDrTrack.Zones[23] + MyDrTrack.Zones[24] 
        return (wp in curva) 

    #----------------------------------------------------------------------------------------------------
    # Dice si es Curva 6 Right
    @staticmethod
    def isCurva6R(wp):
        curva = MyDrTrack.Zones[28] + MyDrTrack.Zones[29]
        return (wp in curva) 
    

    #----------------------------------------------------------------------------------------------------
    # Dice si es una Recta
    @staticmethod
    def isRecta(wp):
        return (MyDrTrack.isRectaIni(wp) or 
                MyDrTrack.isRectaFin(wp) or 
                MyDrTrack.isRecta2(wp)   or 
                MyDrTrack.isRecta3(wp)   or 
                MyDrTrack.isRecta4(wp))

    #----------------------------------------------------------------------------------------------------
    # Dice si es una Curva Left
    @staticmethod
    def isCurvaLeft(wp):
        return (MyDrTrack.isCurva1L(wp) or 
                MyDrTrack.isCurva4L(wp) or 
                MyDrTrack.isCurva5L(wp))

    #----------------------------------------------------------------------------------------------------
    # Dice si es una Curva Right
    @staticmethod
    def isCurvaRight(wp):
        return (MyDrTrack.isCurva2R(wp) or 
                MyDrTrack.isCurva3R(wp) or 
                MyDrTrack.isCurva6R(wp))

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
    def xSteeringCastigo(steering_angle):
        STEERING_THRESHOLD_ABS   =  15
        steering = abs(steering_angle) 
        if steering > STEERING_THRESHOLD_ABS:
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
        

        isLap_n1, isLap_n2, isLap_n3 = MyDrTrack.isLap(track_length)

        
        #-----------[ Distancia a la Racing Line] -------------------

        racingLine = MyRacingLine.RACING_LINE

        cercaUno, cercaDos = Util.racingPointsCercanos([x, y], racingLine)

        dist = Util.distanciaRacingLine([x, y], cercaUno, cercaDos)

        REWARD = 1

        ## Recompensa por el waypoint ##
        wp_reward = max(1 - (dist/(track_width*0.5)), VALUE_ZERO)
        REWARD += wp_reward


        #-----[Velocidad]---------------------------------------------------------
        ## Le sumo el reward por menor gap
        
        speed_deseada = cercaUno[2]
        if MyDrTrack.isRectaVelozR3(closest_waypoints) or MyDrTrack.isRectaVelozR4(closest_waypoints):
            speed_deseada *= 1.16

        REWARD *= MyDrTrack.xSpeedCastigo(speed, speed_deseada)        


        #-----[Recta Final]---------------------------------------------------
        ## Lo Castigo si el gap esta muy lejos de 4.0 en la recta final
        isRectaFin   = MyDrTrack.isRectaFin(closest_waypoints)
        if isRectaFin and isLap_n3:
            speed_deseada = 4.0
            REWARD *= MyDrTrack.xSpeedCastigo(speed, speed_deseada)
            REWARD *= MyDrTrack.xSteeringCastigo(steering_angle)



        #-----[Recta Veloz]---------------------------------------------------
        # Recta veloz R3
        if MyDrTrack.isRectaVelozR3(closest_waypoints):
            speed_deseada = 2.8
            REWARD *= MyDrTrack.xSpeedPremio(speed, speed_deseada)
            REWARD *= MyDrTrack.xSteeringCastigo(steering_angle)
    
        #-----[Recta Veloz]---------------------------------------------------
        # Recta veloz R4
        if MyDrTrack.isRectaVelozR4(closest_waypoints):
            speed_deseada = 3.4
            REWARD *= MyDrTrack.xSpeedPremio(speed, speed_deseada)
            REWARD *= MyDrTrack.xSteeringCastigo(steering_angle)


                
        ## Zero recompensa si off track ##
        if all_wheels_on_track == False:
            REWARD = VALUE_ZERO
            
        return float(REWARD)

#20230831 con Web Console (Wip Final)
myDR = MyDeepRacerClass()

def reward_function(params):
    return myDR.rewardFunction_vZ02(params)
    
    
    
