import math




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
        
        cl = abs(Util._distXY(auto[0],   auto[1],   wCerca_next[0],  wCerca_next[1] ))
        cw = abs(Util._distXY(auto[0],   auto[1],   wCerca[0],       wCerca[1]      ))
        ww = abs(Util._distXY(wCerca[0], wCerca[1], wCerca_next[0],  wCerca_next[1] ))
        
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
            dist = Util._distXY(racingLine[i][0], racingLine[i][1], wp[0],  wp[1])
            dUno.append(dist)
            dDos.append(dist)

        cercaIdxUno = dUno.index(min(dUno))


        dDos[cercaIdxUno] = MAX_VALUE 

        cercaIdxDos = dDos.index(min(dDos))

        cercaUno = racingLine[cercaIdxUno]
        cercaDos = racingLine[cercaIdxDos]

        return [cercaUno, cercaDos]
    

    #----------------------------------------------------------------------------------------------------
    # _distXY: Distancias entre los puntos A y B
    # _diffWP: Diferencia entre los waypoints W1 y W2

    _distXY = lambda x1, y1, x2, y2 : abs(abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

    _diffWP = lambda w1, w2 : 2*(w1**2)*(w2**2) - (w1**4)

    

class MyRacingLine:

    wp  = lambda wp : MyRacingLine.RACING_LINE[wp]
    wpX = lambda wp : MyRacingLine.RACING_LINE[wp][0]
    wpY = lambda wp : MyRacingLine.RACING_LINE[wp][1]
    wpS = lambda wp : MyRacingLine.RACING_LINE[wp][2]
    wpT = lambda wp : MyRacingLine.RACING_LINE[wp][3]
       
    # sept 2023,Roger Super Raceway	60.17m	Clockwise  (2022_september_pro_cw)
    # Optimal racing line (x, y, velocidad)
    RACING_LINE = [
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

    #-----------[  RACING LINE - END  ]-------------------

#-----------[  DATA  ]------------------------------------

    # # sept 2023	Roger Super Raceway	60.17m	Clockwise  (2022_september_pro_cw)

LAP_LENGHT = 60.17
LAP_WIDTH  = 01.07

MAX_VALUE  = 1e3
ZERO_VALUE = 1e-3
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
        
        [CURVA_03_LL_ZONA   , 57,58,59,60,61,62,63,64],   # Vel 1.45 - 1.3


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
    isRecta = lambda wp : (Track.isz(RECTA_01, wp) or 
                           Track.isz(RECTA_02, wp) or 
                           Track.isz(RECTA_03, wp) or 
                           Track.isz(RECTA_04, wp))

    #----------------------------------------------------------------------------------------------------
    # Dice si es una Curva Left
    isCurvaLeft  = lambda wp : (Track.isz(CURVA_03_LL, wp) or 
                                Track.isz(CURVA_06_LL, wp))

    #----------------------------------------------------------------------------------------------------
    # Dice si es una Curva Right
    isCurvaRight = lambda wp : (Track.isz(CURVA_01_RR, wp) or 
                                Track.isz(CURVA_02_RR, wp) or 
                                Track.isz(CURVA_04_RR, wp) or 
                                Track.isz(CURVA_05_RR, wp) or 
                                Track.isz(CURVA_07_RR, wp) or 
                                Track.isz(CURVA_08_RR, wp))

    #----------------------------------------------------------------------------------------------------
    # Speed Castigo - TDD:  reward_TDD_Track.py - test_xSpeedCastigo
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

        GF = [ "nn",  "nn",  ZERO_VALUE ]

        for e in gapVel:
            if  gap  >= e[0] and gap < e[1]:
                GF = e

        PUNISH = GF[2]

        #-------------------------------------------------------------
        if MODE_DEBUG:
            try:
                print("Track.xSpeedCastigo(speed=", speed, ", speed_deseada=", speed_deseada, "): gap -> [",GF[0],",",GF[1],",",GF[2],"]")
            except Exception as e:
                print("Excepcion e:", e)


        return PUNISH


    #----------------------------------------------------------------------------------------------------
    # Steering Castigo - TDD:  reward_TDD_Track.py - test_xSpeedCastigo
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
    #                            TDD:  reward_TDD_Track.py - test_xSpeedCastigo
    @staticmethod
    def _direccionPista(params):
       
        waypoints         = params['waypoints']
        closest_waypoints = params['closest_waypoints']

        wpNext = waypoints[closest_waypoints[1]]
        wpPrev = waypoints[closest_waypoints[0]]

        dirPista = math.degrees(math.atan2(wpNext[1] - wpPrev[1], 
                                           wpNext[0] - wpPrev[0]))

        #-------------------------------------------------------------
        if MODE_DEBUG:
            try:
                print("Track._direccionPista(closest_waypoints=", closest_waypoints, "): wpNext=",wpNext,", wpPrev=",wpPrev,", dirPista=", dirPista)
            except Exception as e:
                print("Excepcion e:", e)

        return dirPista

    #----------------------------------------------------------------------------------------------------
    # Castigo por Heading vs DirPista   - TDD:  reward_TDD_Track.py - test_xHeadingCastigo
    @staticmethod
    def xHeadingCastigo(params, DIRECCION_ABS_VAL, castigo=ZERO_VALUE):
       
        heading = params['heading']

        dirPista = Track._direccionPista(params) 

        dirDiff = abs(dirPista - heading)

        PUNISH = 1

        if dirDiff > DIRECCION_ABS_VAL:
            PUNISH= castigo

        #-------------------------------------------------------------
        if MODE_DEBUG:
            try:
                print("Track.xHeadingCastigo(heading=", heading, ", K,c=",DIRECCION_ABS_VAL, castigo,"): [ dirPista=", dirPista, ", dirDiff=", dirDiff, "] -> PUNISH=",PUNISH) 
            except Exception as e:
                print("Excepcion e:", e)

        return PUNISH


def reward_function(params):
    '''
    Example of rewarding the agent to stay inside the two borders of the track
    '''
    
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

    prev_wp = closest_waypoints[0]
    next_wp = closest_waypoints[1]

    xw = MyRacingLine.wpX(next_wp)
    yw = MyRacingLine.wpY(next_wp)

    dist = Util._distXY(x, y, xw, yw)

    dirPista = Track._direccionPista(params) 


    # Mar recompensa en Cruva Tres y Seis
    isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, next_wp)
    isZonaCurvaSeis   = Track.isz(CURVA_06_LL_ZONA, next_wp)





    if MODE_DEBUG:
        try:
            if (next_wp < 5):
                print("waypoints=", waypoints)

            print("closest_waypoints=", closest_waypoints, "(x, y, speed)=[", x, ",", y, ",", speed, "]", 
                              "dist=", dist,
                            "curva3=", isZonaCurvaTres, 
                            "curva6=", isZonaCurvaSeis) 
             
            print("steering_angle=", steering_angle, "heading=", heading, "dirPista=", dirPista,
                    "distance_from_center=", distance_from_center, "progress=",  progress)
            
        except Exception as e:
            print("Excepcion e:", e)

    



    # Por defaul, la menor recompensa
    reward = ZERO_VALUE

    # Se le da recompensa si el agente no está Off Track pero dentro de los bordes
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0


    # Si es una recta, que controle el Heading esté cerca de la dirección de la pista (20 grados max)
    if Track.isRecta:
        reward *= Track.xHeadingCastigo(params, 20)



    # Si es la curva tres bajar la velocidad deseada a la de la referencia
    if isZonaCurvaTres or isZonaCurvaSeis:
        
        speed_deseada = MyRacingLine.wpS(next_wp)
        reward *= Track.xSpeedCastigo(speed, speed_deseada)

        distReward = lambda d : 1 - dist/LAP_WIDTH
        reward *= 1 - distReward




    
    return float(reward)


