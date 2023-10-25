import math

MAX_VALUE  = 1
ZERO_VALUE = 1e-3
MODE_DEBUG = True


class Track:

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
                print(f"Track._direccionPista(closest_waypoints={closest_waypoints}): wpNext={wpNext}, wpPrev={wpPrev}, dirPista={dirPista}")
            except Exception as e:
                print("Excepcion e:", e)

        return dirPista
    


class Reward:

    BASE_VALUE_20 = 0.20
    BASE_VALUE_40 = 0.40
    BASE_VALUE_60 = 0.60
    BASE_VALUE_80 = 0.80

    #----------------------------------------------------------------------------------------------------
    # Se le da recompensa si el agente no está Off Track pero dentro de los bordes
    @staticmethod
    def fn_inside_track(params, reward_function = ZERO_VALUE):

        # Read input parameters
        all_wheels_on_track = params['all_wheels_on_track']
        distance_from_center = params['distance_from_center']
        track_width = params['track_width']
        
        # Reward if is between borders
        if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
            reward_function = 1.0

        return reward_function
    

    #----------------------------------------------------------------------------------------------------
    # Se le da recompensa si el agente no está Off Track pero dentro de los bordes
    @staticmethod
    def fn_abs_steering(params, reward_function = MAX_VALUE):

        # Params for steering eval
        abs_steering = abs(params['steering_angle'])
    
        # Punish if the car is steering low
        ABS_STEERING_THRESHOLD = 15
        if abs_steering >= ABS_STEERING_THRESHOLD:
            reward_function *= Reward.BASE_VALUE_80
           
        return reward_function

    #----------------------------------------------------------------------------------------------------
    # Castigo por Heading vs DirPista   - TDD:  fn_diff_heading_track.py - fn_rectas_heading
    @staticmethod
    def fn_diff_heading_track(params, reward_function = MAX_VALUE):
       
        heading = params['heading']

        dirPista = Track._direccionPista(params) 

        dirDiff = abs(dirPista - heading)

        if dirDiff > 180:
           dirDiff = 360 - dirDiff
            
        reward_function = ZERO_VALUE

        # Punish if heading vs track is low
        ABS_DIFF_DEGREE_THRESHOLD = 10

        if dirDiff >= ABS_DIFF_DEGREE_THRESHOLD:
            reward_function *= Reward.BASE_VALUE_60

        return reward_function
                   

        

def reward_function(params):

    reward = 1e-3

    reward_fn_01 = Reward.fn_inside_track(params, reward)

    reward_fn_02 = Reward.fn_abs_steering(params, reward_fn_01)

    # reward_fn_03 = Reward.fn_diff_heading_track(params, reward_fn_02)

    reward = reward_fn_02

    return float(reward)


