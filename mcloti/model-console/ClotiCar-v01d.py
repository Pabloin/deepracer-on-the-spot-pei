import math

# Track DBro Super Raceway
#       57.89 meters	
#       1.07 meters


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


   
##
# Similar a:
# https://www.linkedin.com/pulse/samples-reward-functions-aws-deepracer-bahman-javadi
# y a un par de:
    # https://refactored.ai/microcourse/notebook?path=content%2FDeepRacer%2FAWS_DeepRacer_Reward_function_Additional_material.ipynb
    # IDEM TO
    # https://wiki.deepracing.io/Training_the_AWS_DeepRacer
# Y contiene a:
#    https://github.com/sasasavic82/deepracer-reward/blob/master/model/reward_v1.py



# Nota ... la otra corriente de la hipotenusa es
#    https://everdark.github.io/k9/projects/deepracer_2020/deepracer_2020.html
# que esta mas claro en:
#    https://wiki.deepracing.io/Training_the_AWS_DeepRacer
#

        # rabbit = [waypoints[closest_waypoints+1][0],waypoints[closest_waypoints+1][1]]

        # radius = math.hypot(x - rabbit[0], y - rabbit[1])

        # pointing[0] = x + (radius * math.cos(car_orientation))
        # pointing[1] = y + (radius * math.sin(car_orientation))

        # vector_delta = math.hypot(pointing[0] - rabbit[0], pointing[1] - rabbit[1])




# De un Post borrado pero con Time Machine
#
# (B-Sharp)
# https://medium.com/proud2becloud/deepracer-our-journey-to-the-top-ten-257ff69922e
# https://web.archive.org/web/20200905141829/https://medium.com/proud2becloud/deepracer-our-journey-to-the-top-ten-257ff69922e
#
# Hoping that there will soon be new opportunities to get on track, we want to share some of our notes with you:

# It is better to use a machine learning model specific to the track on which you want to compete;
# It is not strictly necessary to train a model for more than eight consecutive hours but, to obtain record times, it becomes essential;
# It is always possible to increase confidence by changing the car’s degrees of freedom;
# Using Waypoints allows you to outline the ideal path;
# To gain those thousandths of a second that make the difference, you can manually vary the speed of the machine during the laps.


