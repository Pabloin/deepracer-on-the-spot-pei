from reward_function import \
         LAP_LENGHT, LAP_WIDTH,  \
         VALUE_MAX_, VALUE_ZERO, \
         MODE_DEBUG, \
         RECTA_01, RECTA_02, RECTA_03, RECTA_04, RECTA_INI, RECTA_FIN, \
         CURVA_01_RR, CURVA_02_RR, CURVA_03_LL, CURVA_03_LL_ZONA,  \
         CURVA_04_RR, CURVA_05_RR, CURVA_06_LL, CURVA_06_LL_ZONA,  \
         CURVA_07_RR, CURVA_08_RR, \
         PATH_01, PATH_02, PATH_03, PATH_04, PATH_05       


from reward_function import Util
from reward_function import MyRacingLine
from reward_function import Track

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







