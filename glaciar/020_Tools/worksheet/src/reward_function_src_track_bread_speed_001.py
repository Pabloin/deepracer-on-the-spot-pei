# Source URL: https://github.com/dp770/aws_deepracer_worksheet/blob/main/src/reward_function.py

# Raceline: 2022_june_open_ccw-1500-8-2023-12-24-034238
# Name:  reward_function_track_bread_speed_001


import math
import numpy as np

# constants
MIN_SPEED = 2.1                     # Model specific. Critical to keep in sync with model's actions space
MAX_SPEED = 4.0                     # Model specific. Critical to keep in sync with model's actions space
MAX_STEERING = 30.0                 # Model specific. Critical to keep in sync with model's actions space
MAX_DIRECTION_DIFF = 30.0
MAX_STEPS_TO_DECAY_PENALTY = 0      # Value of zero or below disables penalty for having wheels off track
MAX_STEPS_TO_PROGRESS_RATIO = 1.8   # Desired maximum number of steps to be taken for 1% of progress
RACING_LINE_SMOOTHING_STEPS = 1     # Track specific. Critical to keep in sync with optimal racing line
RACING_LINE_WIDTH_FREE_ZONE = 0.10  # Percentage of racing line width for 100% of "being on track" reward
RACING_LINE_WIDTH_SAFE_ZONE = 0.25  # Percentage of racing line width for distance relative "being on track" reward
RACING_LINE_VS_CENTRAL_LINE = 0.85  # Number in range of [0, 1]. Zero forces to follow central line, 1 - racing line
SENSITIVITY_EXP_CNT_DISTANCE = 3.00  # Higher number gives more freedom on the track, can cause zig-zags
SENSITIVITY_EXP_ACTION_SPEED = 3.00  # Higher number increases penalty for low speed
SENSITIVITY_EXP_ACTION_STEER = 0.70  # Higher number decreases penalty for high steering
SENSITIVITY_EXP_DIR_STEERING = 2.00  # Lower number accelerates penalty increase for not following track direction
TOTAL_PENALTY_ON_OFF_TRACK = 0.999999  # Maximum penalty in percentage of total reward for being off track
TOTAL_PENALTY_ON_BAD_SPEED = 0.500000  # Maximum penalty in percentage of total reward for being off track
TOTAL_PENALTY_ON_OFF_DIR_STEER = 0.35  # Maximum penalty in percentage of total reward for off directional steering
REWARD_WEIGHT_PROG_STEP = 35
REWARD_WEIGHT_EXP_SPEED = 25
REWARD_WEIGHT_DIR_STEER = 20
REWARD_WEIGHT_ON_TRACK = 15
MAX_TOTAL_REWARD = REWARD_WEIGHT_ON_TRACK + REWARD_WEIGHT_PROG_STEP + REWARD_WEIGHT_DIR_STEER + REWARD_WEIGHT_EXP_SPEED

# static





# smoothed_central_line = None
# smoothed_central_line = track_smoothed


smoothed_central_line = [
       [ 2.16828134,  2.21892651],
       [ 2.04689848,  2.17238402],
       [ 1.92552027,  2.12582943],
       [ 1.76541603,  2.06442147],
       [ 1.48393351,  1.95645797],
       [ 1.20244902,  1.84850049],
       [ 0.92096415,  1.74054503],
       [ 0.63947915,  1.63258952],
       [ 0.35799369,  1.52463502],
       [ 0.07650754,  1.41668251],
       [-0.20497798,  1.3087281 ],
       [-0.48646125,  1.20076805],
       [-0.76794818,  1.09281757],
       [-1.04944903,  0.98490234],
       [-1.33094001,  0.87696135],
       [-1.61194727,  0.77210868],
       [-1.8908527 ,  0.68049174],
       [-2.16537828,  0.61077077],
       [-2.43291575,  0.5693215 ],
       [-2.6908004 ,  0.56023331],
       [-2.9363418 ,  0.58600163],
       [-3.166501  ,  0.64862924],
       [-3.37740431,  0.75031829],
       [-3.56292843,  0.8946988 ],
       [-3.72460536,  1.07285234],
       [-3.86536675,  1.27730761],
       [-3.9899945 ,  1.50053344],
       [-4.105111  ,  1.73434347],
       [-4.23639434,  1.96260524],
       [-4.38318498,  2.16937199],
       [-4.54718641,  2.34872102],
       [-4.72840017,  2.49563264],
       [-4.92548618,  2.60535774],
       [-5.13661547,  2.66786482],
       [-5.35487597,  2.68668542],
       [-5.57520147,  2.66409745],
       [-5.79330404,  2.60155472],
       [-6.00513661,  2.49995112],
       [-6.2065774 ,  2.36000931],
       [-6.39328539,  2.18274316],
       [-6.56079175,  1.97008564],
       [-6.704788  ,  1.72546123],
       [-6.82161001,  1.45441406],
       [-6.9089725 ,  1.16604853],
       [-6.96399586,  0.87479493],
       [-6.98806618,  0.5862607 ],
       [-6.9834405 ,  0.30249471],
       [-6.95202747,  0.0247616 ],
       [-6.89522234, -0.24594393],
       [-6.81403745, -0.50869613],
       [-6.70917549, -0.76251139],
       [-6.58110977, -1.00623731],
       [-6.43020181, -1.23843335],
       [-6.25706064, -1.45736381],
       [-6.06258554, -1.6608309 ],
       [-5.84847721, -1.84643332],
       [-5.61723692, -2.01180917],
       [-5.37203425, -2.15514537],
       [-5.11616917, -2.2753849 ],
       [-4.85263637, -2.37225538],
       [-4.58387811, -2.44610937],
       [-4.31173845, -2.4977187 ],
       [-4.03752274, -2.52785274],
       [-3.76215231, -2.53719673],
       [-3.48628759, -2.52626152],
       [-3.21039693, -2.49718149],
       [-2.93476693, -2.45136339],
       [-2.65959336, -2.39014097],
       [-2.385011  , -2.31480861],
       [-2.11110896, -2.22665974],
       [-1.83793251, -2.12709058],
       [-1.56548708, -2.01757005],
       [-1.29373736, -1.89966612],
       [-1.02259713, -1.7751397 ],
       [-0.75193665, -1.64583113],
       [-0.48158221, -1.51367003],
       [-0.21125579, -1.38247238],
       [ 0.05941122, -1.25889416],
       [ 0.33019669, -1.14924932],
       [ 0.60017471, -1.05919939],
       [ 0.86780877, -0.99334849],
       [ 1.13110274, -0.95521398],
       [ 1.38772372, -0.94732217],
       [ 1.63503886, -0.97149153],
       [ 1.87003784, -1.02915468],
       [ 2.08910865, -1.12167684],
       [ 2.28755336, -1.25069536],
       [ 2.45648523, -1.42078704],
       [ 2.60236877, -1.61750834],
       [ 2.73541152, -1.82797992],
       [ 2.87887003, -2.03954146],
       [ 3.03186615, -2.24207857],
       [ 3.19732761, -2.43207169],
       [ 3.37783575, -2.60575656],
       [ 3.58067017, -2.75177085],
       [ 3.8026104 , -2.8691698 ],
       [ 4.04055793, -2.95693983],
       [ 4.29130994, -3.01383828],
       [ 4.55128114, -3.03870732],
       [ 4.81645091, -3.03068964],
       [ 5.08242381, -2.98942925],
       [ 5.34461469, -2.91531546],
       [ 5.59854552, -2.80953674],
       [ 5.84014006, -2.67398557],
       [ 6.06594796, -2.51107957],
       [ 6.27335313, -2.32364208],
       [ 6.46056015, -2.1145811 ],
       [ 6.62642916, -1.88664747],
       [ 6.77032044, -1.64235873],
       [ 6.89190547, -1.38396144],
       [ 6.99102545, -1.11347454],
       [ 7.06760874, -0.83277897],
       [ 7.12154199, -0.54370235],
       [ 7.15282634, -0.24822893],
       [ 7.16157472,  0.05133401],
       [ 7.14814057,  0.35211089],
       [ 7.11332909,  0.65114071],
       [ 7.0568198 ,  0.94511072],
       [ 6.97774506,  1.22962613],
       [ 6.87614858,  1.50060368],
       [ 6.7526832 ,  1.75475949],
       [ 6.60830231,  1.98948059],
       [ 6.4441169 ,  2.20264051],
       [ 6.26124795,  2.39234099],
       [ 6.06080098,  2.55673693],
       [ 5.84373361,  2.69360999],
       [ 5.6110312 ,  2.80024732],
       [ 5.36448345,  2.87482741],
       [ 5.10767829,  2.92076923],
       [ 4.84280697,  2.93969738],
       [ 4.57172212,  2.93327781],
       [ 4.29605045,  2.90339902],
       [ 4.01722553,  2.85227832],
       [ 3.73648746,  2.78259572],
       [ 3.45484122,  2.69754923],
       [ 3.17299694,  2.60080943],
       [ 2.89132202,  2.49634355],
       [ 2.60988247,  2.38825047],
       [ 2.32839048,  2.28031802],
       [ 2.16828134,  2.21892651]]
    



was_off_track_at_step = -MAX_STEPS_TO_DECAY_PENALTY
previous_steps_reward = MAX_TOTAL_REWARD


# Range [-180:+180]
def calc_slope(prev_point, next_point):
    return math.degrees(math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]))


# Range [0:180]
def calc_direction_diff(steering, heading, track_direction):
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = steering + heading - track_direction
    if direction_diff > 180.0:
        direction_diff = direction_diff - 360.0
    if direction_diff < -180.0:
        direction_diff = direction_diff + 360.0
    return abs(direction_diff)


# Returns distance between two points in meters
def calc_distance(prev_point, next_point):
    delta_x = next_point[0] - prev_point[0]
    delta_y = next_point[1] - prev_point[1]
    return math.hypot(delta_x, delta_y)


def smooth_central_line(center_line, max_offset, pp=0.10, p=0.05, c=0.70, n=0.05, nn=0.10, iterations=72, skip_step=1):
    if max_offset < 0.0001:
        return center_line
    if skip_step < 1:
        skip_step = 1
    smoothed_line = center_line
    for i in range(0, iterations):
        smoothed_line = smooth_central_line_internal(center_line, max_offset, smoothed_line, pp, p, c, n, nn, skip_step)
    return smoothed_line


def smooth_central_line_internal(center_line, max_offset, smoothed_line, pp, p, c, n, nn, skip_step):
    length = len(center_line)
    new_line = [[0.0 for _ in range(2)] for _ in range(length)]
    for i in range(0, length):
        wpp = smoothed_line[(i - 2 * skip_step + length) % length]
        wp = smoothed_line[(i - skip_step + length) % length]
        wc = smoothed_line[i]
        wn = smoothed_line[(i + skip_step) % length]
        wnn = smoothed_line[(i + 2 * skip_step) % length]
        new_line[i][0] = pp * wpp[0] + p * wp[0] + c * wc[0] + n * wn[0] + nn * wnn[0]
        new_line[i][1] = pp * wpp[1] + p * wp[1] + c * wc[1] + n * wn[1] + nn * wnn[1]
        while calc_distance(new_line[i], center_line[i]) >= max_offset:
            new_line[i][0] = (0.98 * new_line[i][0]) + (0.02 * center_line[i][0])
            new_line[i][1] = (0.98 * new_line[i][1]) + (0.02 * center_line[i][1])
    return new_line


# Calculate distance between current point and closest point on line between prev_point and next_point
def calc_distance_from_line(curr_point, prev_point, next_point):
    distance_cp_to_pp = calc_distance(curr_point, prev_point)  # b
    distance_cp_to_np = calc_distance(curr_point, next_point)  # a
    distance_pp_to_np = calc_distance(prev_point, next_point)  # c
    # cos A = (b^2 + c^2 - a^2) / 2bc
    angle_pp = math.acos((distance_cp_to_pp * distance_cp_to_pp + distance_pp_to_np * distance_pp_to_np
                          - distance_cp_to_np * distance_cp_to_np) / (2 * distance_cp_to_pp * distance_pp_to_np))
    # b / sin(Pi/2) = d / sin(A)
    return distance_cp_to_pp * math.sin(angle_pp)


def ema(prev, new, period):
    k = 2.0 / (1.0 + period)
    return (new - prev) * k + prev


# Reward function expected by AWS DeepRacer API
def reward_function(params):
    track_width = params['track_width']
    waypoints = params['waypoints']
    # initialize central line
    global smoothed_central_line

    # re-initialize was_off_track_at_step
    global was_off_track_at_step
    steps = params['steps']
    if steps < was_off_track_at_step:
        was_off_track_at_step = -MAX_STEPS_TO_DECAY_PENALTY
    if not params['all_wheels_on_track']:
        was_off_track_at_step = steps

    global previous_steps_reward
    if steps <= 2:
        previous_steps_reward = MAX_TOTAL_REWARD

    # Calculate penalty for wheels being or have recently been off track
    wheels_off_track_penalty = 1.0
    if MAX_STEPS_TO_DECAY_PENALTY > 0:
        wheels_off_track_penalty = min(steps - was_off_track_at_step, MAX_STEPS_TO_DECAY_PENALTY) / (
            1.0 * MAX_STEPS_TO_DECAY_PENALTY)

    # Reward on directional move to the next milestone
    wp_length = len(smoothed_central_line)
    wp_indices = params['closest_waypoints']
    curr_point = [params['x'], params['y']]
    prev_point = smoothed_central_line[wp_indices[0]]
    next_point_1 = smoothed_central_line[(wp_indices[1] + 1) % wp_length]
    next_point_2 = smoothed_central_line[(wp_indices[1] + 2) % wp_length]
    next_point_3 = smoothed_central_line[(wp_indices[1] + 3) % wp_length]
    track_direction_1 = calc_slope(prev_point, next_point_1)
    track_direction_2 = calc_slope(prev_point, next_point_2)
    track_direction_3 = calc_slope(prev_point, next_point_3)

    heading = params['heading']  # Range: -180:+180
    steering = params['steering_angle']  # Range: -30:30
    direction_diff_ratio = (
            0.20 * min((calc_direction_diff(steering, heading, track_direction_1) / MAX_DIRECTION_DIFF), 1.00) +
            0.30 * min((calc_direction_diff(steering, heading, track_direction_2) / MAX_DIRECTION_DIFF), 1.00) +
            0.50 * min((calc_direction_diff(steering, heading, track_direction_3) / MAX_DIRECTION_DIFF), 1.00))
    dir_steering_ratio = 1.0 - pow(direction_diff_ratio, SENSITIVITY_EXP_DIR_STEERING)
    reward_dir_steering = REWARD_WEIGHT_DIR_STEER * dir_steering_ratio

    # Reward on speed relevant to track's direction
    speed = params['speed']  # Range: 0.0:4.0
    expect_speed_ratio = 1.0 - min(abs(track_direction_1 - track_direction_3), MAX_DIRECTION_DIFF) / MAX_DIRECTION_DIFF
    actual_speed_ratio = max(min(speed - MIN_SPEED, 0), MAX_SPEED - MIN_SPEED) / (MAX_SPEED - MIN_SPEED)
    speed_ratio = 1.0 - abs(expect_speed_ratio - actual_speed_ratio)
    reward_exp_speed = REWARD_WEIGHT_EXP_SPEED * pow(speed_ratio, SENSITIVITY_EXP_ACTION_SPEED)

    # Reward on close distance to the racing line
    free_zone = track_width * RACING_LINE_WIDTH_FREE_ZONE * 0.5
    safe_zone = track_width * RACING_LINE_WIDTH_SAFE_ZONE * 0.5
    dislocation = calc_distance_from_line(curr_point, prev_point, next_point_1)
    on_track_ratio = 0.0
    if dislocation <= free_zone:
        on_track_ratio = 1.0
    elif dislocation <= safe_zone:
        on_track_ratio = 1.0 - pow(dislocation / safe_zone, SENSITIVITY_EXP_CNT_DISTANCE)
    reward_on_track = on_track_ratio * REWARD_WEIGHT_ON_TRACK

    # Reward on good progress per step
    progress = params['progress']
    reward_prog_step = REWARD_WEIGHT_PROG_STEP * min(1.0, MAX_STEPS_TO_PROGRESS_RATIO * (progress / steps))

    reward_total = reward_on_track + reward_exp_speed + reward_dir_steering + reward_prog_step
    reward_total -= reward_total * (1.0 - dir_steering_ratio) * TOTAL_PENALTY_ON_OFF_DIR_STEER
    reward_total -= reward_total * (1.0 - on_track_ratio) * TOTAL_PENALTY_ON_OFF_TRACK
    reward_total -= reward_total * (1.0 - speed_ratio) * TOTAL_PENALTY_ON_BAD_SPEED
    reward_total *= wheels_off_track_penalty


    # Hay un error que da por:
    #    "Typeerror: can only join an iterable"


    # print("rewards:" + (20 * "{:.4f}," + "{:.4f}").format(reward_total,
    #     wheels_off_track_penalty, reward_on_track, reward_exp_speed, reward_dir_steering, reward_prog_step,
    #     dislocation, track_direction_1, track_direction_2, track_direction_3, direction_diff_ratio,
    #     waypoints[wp_indices[0]][0], waypoints[wp_indices[0]][1], prev_point[0], prev_point[1],
    #     next_point_1[0], next_point_1[1], next_point_2[0], next_point_2[1], next_point_3[0], next_point_3[1]))

    previous_steps_reward = ema(previous_steps_reward, reward_total, 3)
    return float(0.0000001 + previous_steps_reward)
