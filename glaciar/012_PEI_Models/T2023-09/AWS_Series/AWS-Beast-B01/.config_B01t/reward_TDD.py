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
from reward_function import Reward
from reward_TDD_params import params


print('Hola')

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



# Distancia entre dos Waypoints consecutivos

# closest_waypoints=[39, 40]): wpNext=(-5.565105438232422, -5.533783912658691), wpPrev=(-5.300961494445801, -5.678500175476074)

wpX_next = -5.565105438232422
wpY_next = -5.533783912658691

wpX_prev = -5.300961494445801
wpY_prev = -5.678500175476074


dist = Util._distXY(wpX_next, wpY_next, wpX_prev, wpY_prev) 

print("dist closest_waypoints=[39, 40]):", dist)


#closest_waypoints=[49, 50]): wpNext=(-7.42689847946167, -3.6140815019607544), wpPrev=(-7.5350682735443115, -3.8938859701156616)

wpX_next = -7.42689847946167
wpY_next = -3.6140815019607544

wpX_prev = -7.5350682735443115
wpY_prev = -3.8938859701156616


dist = Util._distXY(wpX_next, wpY_next, wpX_prev, wpY_prev) 

print("dist closest_waypoints=[49, 50]):", dist)



# SIM_TRACE_LOG:19,138,-7.1965,-3.8388,113.7064,-30.00,3.15,[-30.0, 3.1456791077417017],0.0001,False,True,29.7967,50,60.18,415.38,in_progress,0.00

# Track._direccionPista(closest_waypoints=[49, 50]): wpNext=(-7.42689847946167, -3.6140815019607544), wpPrev=(-7.5350682735443115, -3.8938859701156616), dirPista=68.86396372252557

# Util.racingPointsCercanos(xyPoint[-7.202018770586495, -3.82983706969537]): 
#           -> [cercaUno=[-7.13802, -3.84283, 1.53582, 0.15861, 51],0.0653] 
#              [cercaDos=[-7.14163, -3.59361, 1.67981, 0.14838, 52],0.2438]
#
#

# closest_waypoints=[49, 50], (x, y, speed)=[-7.202018770586495,-3.82983706969537,3.6942068275016364]dist=0.27414531623540384curva3= False curva6= False
# steering_angle=-30.0, heading=114.16132328977962, dirPista=68.86396372252557, distance_from_center=0.2875492623963251, steps=139.0, progress=29.807306442903155
# DEBUG_RACING_LINE wp(51-> [-7.284416198730469, -3.348726987838745] - rl([-7.13802, -3.84283, 1.53582, 0.15861, 51]] ->  dist(0.52) ]   
# Track._direccionPista(closest_waypoints=[49, 50]): wpNext=(-7.42689847946167, -3.6140815019607544), wpPrev=(-7.5350682735443115, -3.8938859701156616), dirPista=68.86396372252557
# Track.xHeadingCastigo(heading=114.16132328977962, K,c=20,0.001): [ dirPista=68.86396372252557, dirDiff=45.29735956725405] -> PUNISH=0.001
# Track.castigoPunto(carPunto=[-7.202018770586495, -3.82983706969537], cercaUno=[-7.13802, -3.84283, 1.53582, 0.15861, 51]): dist=0.06530435570835821, gap -> [0.0,0.1,1.0
# Track.xSpeedCastigo(speed=3.6942068275016364, speed_deseada=1.53582): gap -> [2.1,4.0,0.0

#              episode,steps,X,Y,yaw,steer,throttle,action,
#                                       reward,done,all_wheels_on_track,progress,
#                                                   closest_waypoint,track_len,tstamp,episode_status,pause_duration

# SIM_TRACE_LOG:19,139,-7.2020,-3.8298,114.1613,-30.00,3.69,[-30.0, 3.6942068275016364],
#                                       0.0000,False,True,29.8073,
#                                                   50,60.18,415.406,in_progress,0.00



#----------------------------
# Otra con mas distancias ... 

# SIM_TRACE_LOG:19,165,-6.0296,-1.2986,37.3059,30.00,1.72,[30.0, 1.7223045412545273],0.0005,False,True,34.4916,59,60.18,417.155,in_progress,0.00

# Track._direccionPista(closest_waypoints=[59, 60]): wpNext=(-6.041717529296875, -0.9397014677524567), 
#                                                    wpPrev=(-6.179857969284058, -1.2073353230953217), dirPista=62.69927196912729

# isz(CURVA_03_LL_ZONA,60)=True
# Util.racingPointsCercanos(xyPoint[-5.894488400976971, -1.1844722481003302]): 
#           -> [cercaUno=[-6.40752, -1.25239, 1.3, 0.19279, 61],0.5175] 
#              [cercaDos=[-6.40431, -1.01331, 1.3, 0.18392, 62],0.5378]

# closest_waypoints=[59, 60], (x, y, speed)=[-5.894488400976971,-1.1844722481003302,3.4600466866575674]dist=0.6356522658145819curva3= True curva6= False
# steering_angle=-0.02934338123710134, heading=38.8521517048756, dirPista=62.69927196912729, distance_from_center=0.2430962556499666, steps=166.0, progress=34.762768012209875
# 
# DEBUG_RACING_LINE wp(61-> [-5.9454615116119385, -0.6823945939540863] - rl([-6.40752, -1.25239, 1.3, 0.19279, 61]] ->  dist(0.73) ]   
# Track._direccionPista(closest_waypoints=[59, 60]): wpNext=(-6.041717529296875, -0.9397014677524567), wpPrev=(-6.179857969284058, -1.2073353230953217), dirPista=62.69927196912729
# Track.xHeadingCastigo(heading=38.8521517048756, K,c=20,0.001): [ dirPista=62.69927196912729, dirDiff=23.847120264251686] -> PUNISH=0.001
# Track.castigoPunto(carPunto=[-5.894488400976971, -1.1844722481003302], cercaUno=[-6.40752, -1.25239, 1.3, 0.19279, 61]): dist=0.5175077222798045, gap -> [0.5,0.6,0.5
# Track.xSpeedCastigo(speed=3.4600466866575674, speed_deseada=1.3): gap -> [2.1,4.0,0.0

# SIM_TRACE_LOG:19,166,-5.8945,-1.1845,38.8522,-0.03,3.46,[-0.02934338123710134, 3.4600466866575674],0.0000,False,True,34.7628,60,60.18,417.23,in_progress,0.00




#------------
# Mar recompensa en Cruva Tres y Seis

next_wp=91
isCurvaTres   = Track.isCurvaLeft(next_wp)

print("isCurvaTres", isCurvaTres)