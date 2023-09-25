import math

from reward_function import \
         LAP_LENGHT, LAP_WIDTH,  \
         MAX_VALUE, ZERO_VALUE, \
         MODE_DEBUG, \
         RECTA_01, RECTA_02, RECTA_03, RECTA_04, RECTA_INI, RECTA_FIN, \
         CURVA_01_RR, CURVA_02_RR, CURVA_03_LL, CURVA_03_LL_ZONA,  \
         CURVA_04_RR, CURVA_05_RR, CURVA_06_LL, CURVA_06_LL_ZONA,  \
         CURVA_07_RR, CURVA_08_RR, \
         PATH_01, PATH_02, PATH_03, PATH_04, PATH_05       


from reward_function import Util
from reward_function import MyRacingLine
from reward_function import Track
from reward_TDD_params import params

print('Hola')


# closest_waypoints: [1, 2]
# closest_waypoints[1]: 2
# closest_waypoints[0]: 1
# closest_waypoints: 1 2


# x: 4.5960888763624235 y: -4.3378093609562995    next_wp:  4.429752826690674 -4.417214512825012  - wpPrev:  4.654623508453369 -4.217042446136475  - speed:  1.25
# steering_angle:  30.0 heading:  -125.8884993664113 distance_from_center:  0.05128566786655362
# curva3 False curva6 False progress:  0.7063766453562026
# OTRA: x: 4.5960888763624235 y: -4.3378093609562995    next_wp:  4.429752826690674 -4.417214512825012  - wpPrev:  4.654623508453369 -4.217042446136475  - speed:  1.25
# OTRA: steering_angle:  30.0 heading:  -125.8884993664113 distance_from_center:  0.05128566786655362 progress:  0.7063766453562026
# SIM_TRACE_LOG:0,7,4.5961,-4.3378,-125.8885,30.00,1.25,[30.0, 1.25],1.0000,False,True,0.7064,1,60.18,42.173,in_progress,0.00


#SIM_TRACE_LOG:0,1,4.7634,-4.0986,-132.5784,-0.80,2.46,[-0.7983805874334244, 2.455950601998581],0.0000,False,True,0.2331,
# 
# 0,60.18,38.842,prepare,0.00

# next_wp = waypoints[closest_waypoints[1]]
# wpPrev = waypoints[closest_waypoints[0]]

closest_waypoints = [1, 2]

next_wp = [4.429752826690674, -4.417214512825012]    
wpPrev = [4.654623508453369, -4.217042446136475]    



#------------
# Mar recompensa en Cruva Tres y Seis
isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, next_wp)

isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, next_wp)
print("isZonaCurvaTres(", CURVA_03_LL_ZONA, ",", next_wp, ") = ", isZonaCurvaTres )


next_wp=12
isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, next_wp)
print("isZonaCurvaTres(", CURVA_03_LL_ZONA, ",", next_wp, ") = ", isZonaCurvaTres )


next_wp=61
isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, next_wp)
print("isZonaCurvaTres(", CURVA_03_LL_ZONA, ",", next_wp, ") = ", isZonaCurvaTres )


isZonaCurvaSeis   = Track.isz(CURVA_06_LL_ZONA, next_wp)


next_wp=61
print("MyRacingLine[",next_wp,"]", MyRacingLine.rp(next_wp))
print("MyRacingLine[",next_wp,"]", MyRacingLine.rpX(next_wp))
print("MyRacingLine[",next_wp,"]", MyRacingLine.rpY(next_wp))
print("MyRacingLine[",next_wp,"]", MyRacingLine.rpS(next_wp))
print("MyRacingLine[",next_wp,"]", MyRacingLine.rpT(next_wp))
# curva3 False curva6 False

# renglon 61 = (-6.041717529296875, -0.9397014677524567), 
# renglon 61 = [-6.4463, -1.5, 1.3, 0.20338],

next_wp=61
x = -6.041717529296875
y = -0.9397014677524567
b1 = MyRacingLine.rpX(next_wp)
b2 = MyRacingLine.rpY(next_wp)


print("_distXY: ",  Util._distXY(x, y, b1, b2) )
print("_distXY: ",  Util._distXY(x, y, x, y) )
print("_distXY: ",  Util._distXY(b1, b2, x, y) )

dist = Util._distXY(b1, b2, x, y) 

rr = lambda d : dist / LAP_WIDTH

print("dist reward (",dist,"):", rr(dist), "reward: ", 1 - rr(dist) )

dist = 0.47
print("dist reward (",dist,"):", rr(dist), "reward: ", 1 - rr(dist) )

dist = 0.75
print("dist reward (",dist,"):", rr(dist), "reward: ", 1 - rr(dist) )


dist = 0.03
print("dist reward (",dist,"):", rr(dist), "reward: ", 1 - rr(dist) )


dist = 0.0
print("dist reward (",dist,"):", rr(dist), "reward: ", 1 - rr(dist) )


#-----------
next_wp=17
isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, next_wp)
print("isZonaCurvaTres(", CURVA_03_LL_ZONA, ",", next_wp, ") = ", isZonaCurvaTres )


# closest_waypoints= [16, 17] (x, y, speed)=[ 0.7215891450030298 , -6.820596359742561 , 1.25 ] dist= 0.5185205832994217 curva3= False curva6= False
# steering_angle= -30.0 heading= -135.45509757850553 distance_from_center= 0.12350333943277318 progress= 3.340266933267724

eee = [ 0.7215891450030298 , -6.820596359742561 , 1.25 ]
x = eee[0]
y = eee[1]
b1 = MyRacingLine.rpX(next_wp)
b2 = MyRacingLine.rpY(next_wp)

dist = Util._distXY(b1, b2, x, y) 

print("dist reward (",next_wp,"",dist,"):", rr(dist), "reward: ", 1 - rr(dist) )


# heading = params['heading']



closest_waypoints = [16, 17]
wpNext = params.waypoints[closest_waypoints[1]]
wpPrev = params.waypoints[closest_waypoints[0]]

dirPista = math.degrees(math.atan2(wpNext[1] - wpPrev[1], 
                                   wpNext[0] - wpPrev[0]))



heading= -135.45509757850553

dirDiff = abs(dirPista - heading)

print("distPista (",closest_waypoints, "):", dirPista, "heading=",heading,"dirDiff=", dirDiff )
