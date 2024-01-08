from ClotiCar_v01g import CarControl
 

def testCarControl(waypoint, dir, expected): 
    rta = CarControl.direccion_ok(waypoint, dir)
    try:
        assert rta == expected
    except AssertionError as e:
        print(f'Assertion fallo para direccion_ok({waypoint}, {dir}))')
        exit(1)

# Contrloes en OFF
testCarControl(16, CarControl.DIR_L, True)
testCarControl(16, CarControl.DIR_C, True)
testCarControl(16, CarControl.DIR_R, True)


# Contrloes en ON
testCarControl(64, CarControl.DIR_L, True)





def testCarControl_AuX_Side(is_left_of_center, distance_from_center, expected): 

    params = {
        "is_left_of_center"     : is_left_of_center,
        "distance_from_center"  : distance_from_center,
    }
    rta = CarControl.aux_side(params)
    try:
        assert rta == expected
    except AssertionError as e:
        print(f'Assertion fallo para testCarControl_AuX_Side({params}, expected={expected}))')
        exit(1)


testCarControl_AuX_Side(True,  0.05, CarControl.DIR_C)

testCarControl_AuX_Side(True,  0.10, CarControl.DIR_L)
testCarControl_AuX_Side(False, 0.10, CarControl.DIR_R)

testCarControl_AuX_Side(True,  0.20, CarControl.DIR_L)
testCarControl_AuX_Side(False, 0.30, CarControl.DIR_R)




def testCarControl_Reward(wp1, is_left_of_center, distance_from_center, expected): 

    params = {
        "is_left_of_center"     : is_left_of_center,
        "distance_from_center"  : distance_from_center,
    }
    dir = CarControl.aux_side(params)
    
    reward = 1.0
    if not CarControl.direccion_ok(wp1, dir):
        reward *= 0.8

    try:
        assert reward == expected
    except AssertionError as e:
        print(f'Assertion fallo para testCarControl_Reward({wp1}, {params}, expected={expected}))')
        exit(1)


CASTIGAR_REWARD=0.8
NO_CASTIGAR_ESTA_OK=1.0


# ¿Por que castigar aca?
#     El es waypoint que me interesa evaluar ... 
#     No esta en la izquierda, esta en el centro y yo esperaba que este en la izquierda   
testCarControl_Reward(64, False, 0.05, CASTIGAR_REWARD)

#     IDEM al anterior pero está en la derecha y yo esperaba que este en la izquierda   
testCarControl_Reward(64, False, 0.30, CASTIGAR_REWARD)

#     IDEM al anterior pero está en el centro y yo esperaba que este en la izquierda  
testCarControl_Reward(64, True,  0.05, CASTIGAR_REWARD)

#
testCarControl_Reward(64, True,  0.15, NO_CASTIGAR_ESTA_OK)


# IGNORAR
testCarControl_Reward(44, True,   0.15, NO_CASTIGAR_ESTA_OK)
testCarControl_Reward(44, False,  0.15, NO_CASTIGAR_ESTA_OK)

testCarControl_Reward(44, True,   0.05, NO_CASTIGAR_ESTA_OK)
testCarControl_Reward(44, False,  0.05, NO_CASTIGAR_ESTA_OK)


# El 117 castigar si no esta en el centro: 
testCarControl_Reward(117, True,   0.05, NO_CASTIGAR_ESTA_OK)
testCarControl_Reward(117, False,  0.05, NO_CASTIGAR_ESTA_OK)

testCarControl_Reward(117, True,   0.15, CASTIGAR_REWARD)  # Castiga por estar a la izquierda 
testCarControl_Reward(117, False,  0.15, CASTIGAR_REWARD)  # Castiga por estar a la derecha


# El 155 castigar si no esta hacia la izquierda: 
testCarControl_Reward(155, True,  0.15, NO_CASTIGAR_ESTA_OK)
testCarControl_Reward(155, True,  0.05, CASTIGAR_REWARD)  # Castiga por estar a la izquierda pero no lejos del centro
testCarControl_Reward(155, False, 0.05, CASTIGAR_REWARD)  # Castiga por estar a la derecha
testCarControl_Reward(155, False, 0.15, CASTIGAR_REWARD)  # Castiga por estar a la derecha
