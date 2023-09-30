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
from reward_TDD_params import MyParams
from reward_function import reward_function




#----------------------------------
def fn_rectas_heading(heading, closest_waypoints, waypoints=MyParams.waypoints):

    print("\n\n-----------------------\n fn_rectas_heading\n")
    params = {
        "heading"           : heading,
        "waypoints"         : waypoints,
        "closest_waypoints" : closest_waypoints
    }
    reward = Reward.fn_rectas_heading(params, 30)


    print("fn_rectas_heading(",heading,",",closest_waypoints,")", reward)
    print("-----------------------\n")


heading= -110.9658015723231
closest_waypoints= [2, 3]
fn_rectas_heading(heading, closest_waypoints)


heading= 119.07971369710347
closest_waypoints= [32, 33]
fn_rectas_heading(heading, closest_waypoints)



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




#----------------------------------
def test_direccionPista(closest_waypoints, waypoints=MyParams.waypoints):

    print("\n\n-----------------------\n test_direccionPista\n")
    params = {
        "waypoints"         : waypoints,
        "closest_waypoints" : closest_waypoints
    }
    dirAngulos = Track._direccionPista(params)


    print("test_direccionPista(",closest_waypoints,"): dir(Angulos)=", dirAngulos)
    print("-----------------------\n")


closest_waypoints= [32, 33]
test_direccionPista(closest_waypoints)


#----------------------------------
next_wp=63
isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, next_wp)
print("isZonaCurvaTres(", CURVA_03_LL_ZONA, ",", next_wp, ") = ", isZonaCurvaTres )

next_wp=12
isZonaCurvaTres   = Track.isz(CURVA_03_LL_ZONA, next_wp)
print("isZonaCurvaTres(", CURVA_03_LL_ZONA, ",", next_wp, ") = ", isZonaCurvaTres )









#----------------------------------
def test_printPuntos(closest_waypoints, speed, waypoints=MyParams.waypoints):

    print("\n\n-----------------------\n test_printPuntos\n")
    params = {
        "speed"             : speed,
        "waypoints"         : waypoints,
        "closest_waypoints" : closest_waypoints
    }
    dirAngulos = MyRacingLine.printPuntos(params)

    print("\n-----------------------\n printPunto\n")

    prev_wp = closest_waypoints[0]
    next_wp = closest_waypoints[1]

    MyRacingLine.printPunto(waypoints, next_wp, speed)

    # print("test_direccionPista(",closest_waypoints,"): dir(Angulos)=", dirAngulos)
    print("-----------------------\n")



speed=3.9884385764598846
closest_waypoints= [32, 33]
test_printPuntos(closest_waypoints, speed)






# #----------------------------------
# def test_addIdx():

#     print("\n\n-----------------------\n test_addIdx\n")

#     dirAngulos = MyRacingLine.addIdx()

#     print("-----------------------\n")


# speed=3.9884385764598846
# closest_waypoints= [32, 33]
# test_addIdx()




#----------------------------------
def test_racingPointsCercanos(wp):

    print("\n\n-----------------------\n test_racingPointsCercanos\n")
    puntos = Util.racingPointsCercanos(wp)

    print("\n-----------------------\n printPunto\n")


    # print("test_direccionPista(",closest_waypoints,"): dir(Angulos)=", dirAngulos)
    print("-----------------------\n")


x= 4.5960888763624235 
y= -4.3378093609562995 

xyPoint=[x, y]
test_racingPointsCercanos(xyPoint)


#---------------------------------------------
waypoint=50
closest_waypoints= [50, 51]


x=-7.377988610326252
y=-3.4873098237291256 
xyPoint=[x, y]
test_racingPointsCercanos(xyPoint)

x=-7.373047259897509
y=-3.4818414798413038
xyPoint=[x, y]
test_racingPointsCercanos(xyPoint)



x=-7.367953942564247
y=-3.470647788242167
xyPoint=[x, y]
test_racingPointsCercanos(xyPoint)

x=-7.3575201668125
y=-3.4563898954808288
xyPoint=[x, y]
test_racingPointsCercanos(xyPoint)



x= -7.320055285934866
y= -3.4204596895711097
xyPoint=[x, y]
test_racingPointsCercanos(xyPoint)








#----------------------------------
def test_castigoPunto(xyPoint):

    print("\n\n-----------------------\n test_castigoPunto\n")

    cercaUno, cercaDos = Util.racingPointsCercanos([x, y])
    cercaUno_rl = cercaUno[4]
    cercaDos_rl = cercaDos[4]

    castigo = Track.castigoPunto(xyPoint, cercaUno)

    print("\n-----------------------\n castigoPunto\n")

    print(f"test_castigoPunto({xyPoint},{cercaUno}): castigo={castigo}")
    print("-----------------------\n")


x=-7.367953942564247
y=-3.470647788242167
xyPoint=[x, y]
test_castigoPunto(xyPoint)





#----------------------------------
def test_reward_function():

    print("\n\n-----------------------\n test_reward_function\n")

    x=-8.713415188646103
    y=2.8507765531539917
    steps=224.0
    steps=1.25  #???
    heading=75.21663026908212
    progress=43.95628927576247
    distance_from_center=0.23052139701033608
    steering_angle=-13.464126114287648
    closest_waypoints=[77, 78]
    track_length=LAP_LENGHT
    track_width=1.06

    is_left_of_center=True
    all_wheels_on_track=True

    is_offtrack=False
    is_reversed=False

    params = {
        "x"             : x,
        "y"             : y,
        
        "steps"         : steps,
        "speed"         : speed,
        "heading"       : heading,
        "progress"      : progress,
        "heading"       : heading,

        "is_left_of_center": is_left_of_center,
        "all_wheels_on_track" :  all_wheels_on_track, 

        "is_offtrack" : is_offtrack,
        "is_reversed" : is_reversed,
        
        "waypoints" : MyParams.waypoints,

        "distance_from_center"   : distance_from_center,
        "steering_angle"         : steering_angle,
        "closest_waypoints"       : closest_waypoints,
        "track_length"            : track_length,
        "track_width"  : track_width
    }





    rr = reward_function(params)

    print("\n-----------------------\n test_reward_function\n")

    print(f"test_reward_function(params): reward_function={rr}")
    print("-----------------------\n")



test_reward_function()
