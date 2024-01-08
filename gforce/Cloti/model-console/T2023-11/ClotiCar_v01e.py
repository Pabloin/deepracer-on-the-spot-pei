import math

# Expedition Super Loop! Long track at 69.96m (red_star_pro_cw)



def aux_heading_vs_track_angle(params):

    # Params for heading eval
    track_waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    
    # Heading and track_angle closer
    wp1 = track_waypoints[closest_waypoints[1]]
    wp0 = track_waypoints[closest_waypoints[0]]

    track_angle = math.degrees(math.atan2(wp1[1] - wp0[1], wp1[0] - wp0[0]))

    angleDiffernce = abs(track_angle - heading)

    if angleDiffernce > 180:
       angleDiffernce = 360 - angleDiffernce

    return angleDiffernce


def reward_function(params):

    # Params for borders eval
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    is_offtrack = params['is_offtrack']

    # Params for steering eval
    abs_steering = abs(params['steering_angle'])


    # Speed y Progreso
    speed = params['speed']
    progress = params['progress']



    REWARD_ZERO = 1e-3

    # Give a very low reward by default
    reward = 1e-3

    # Si Off track Retorna Zero
    if is_offtrack:
        return REWARD_ZERO

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0


    # Penalize reward if the car is steering too much
    ABS_STEERING_UMBRAL = 15
    if abs_steering > ABS_STEERING_UMBRAL:
        reward *= 0.8


    # Penalize reward heading vs track is high
    ABS_ANGLE_DIFF_UMBRAL = 10

    angleDiffernce = aux_heading_vs_track_angle(params)

    if angleDiffernce > ABS_ANGLE_DIFF_UMBRAL:
        reward *= 0.7

    # Speed y Progreso
    SPEED_UMBRAL = 3
    if speed < SPEED_UMBRAL:
        reward *= 0.8
    if progress == 100:    
        reward += 100

    return float(reward)


