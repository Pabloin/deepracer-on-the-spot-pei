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


#----------------------------------
def test_xHeadingCastigo(heading, closest_waypoints, waypoints=params.waypoints):

    print("\n\n-----------------------\n test_xHeadingCastigo\n")
    params = {
        "heading"           : heading,
        "waypoints"         : waypoints,
        "closest_waypoints" : closest_waypoints
    }
    reward = Track.xHeadingCastigo(params, 30, 1e-3)


    print("xHeadingCastigo(",heading,",",closest_waypoints,")", reward)
    print("-----------------------\n")


heading= -110.9658015723231
closest_waypoints= [2, 3]
test_xHeadingCastigo(heading, closest_waypoints)


heading= 119.07971369710347
closest_waypoints= [32, 33]
test_xHeadingCastigo(heading, closest_waypoints)



#----------------------------------
def test_xSpeedCastigo(speed, speed_deseada):
    
    print("\n\n-----------------------\n test_xSpeedCastigo\n")

    reward = Track.xSpeedCastigo(speed, speed_deseada)


    print("xSpeedCastigo(",speed,",",speed_deseada,") ->", reward)
    print("-----------------------\n")


speed=3.9884385764598846
speed_deseada=1.45015
test_xSpeedCastigo(speed, speed_deseada)


speed=1.25 
speed_deseada=1.45015 
test_xSpeedCastigo(speed, speed_deseada)
