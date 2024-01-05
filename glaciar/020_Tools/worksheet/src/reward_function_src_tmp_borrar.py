# Source URL: https://github.com/dp770/aws_deepracer_worksheet/blob/main/src/reward_function.py
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


# PABLO IN_:
# Track:          BaadalTrack - AmericasGeneratedInclStart
# Raceline: 
# Name:       
# NOTA:  Este código lo pude enviar Ok a evaluar .....
# Debe haber alguna correspondencia entre los waypoints de la pista (196 creo)
# Y la racing line...  (140) porque hubo index out of bounds y cuando cambié la pista ase corrigio... (cambiaron los waypoints...)

raceline_BaadalTrack = np.array([[-5.66000295e+00,  3.95888042e+00],
       [-5.75703549e+00,  3.84409940e+00],
       [-5.85366198e+00,  3.72897654e+00],
       [-5.94980669e+00,  3.61345196e+00],
       [-6.04537553e+00,  3.49744883e+00],
       [-6.14024448e+00,  3.38087404e+00],
       [-6.23428202e+00,  3.26362598e+00],
       [-6.32729857e+00,  3.14556610e+00],
       [-6.41872658e+00,  3.02628407e+00],
       [-6.50781510e+00,  2.90531371e+00],
       [-6.59373833e+00,  2.78226873e+00],
       [-6.67562938e+00,  2.65686392e+00],
       [-6.75258522e+00,  2.52891404e+00],
       [-6.82371015e+00,  2.39835149e+00],
       [-6.88814097e+00,  2.26522689e+00],
       [-6.94508854e+00,  2.12971054e+00],
       [-6.99384877e+00,  1.99207730e+00],
       [-7.03381869e+00,  1.85269237e+00],
       [-7.06450716e+00,  1.71199437e+00],
       [-7.08553627e+00,  1.57047691e+00],
       [-7.09664740e+00,  1.42867050e+00],
       [-7.09760079e+00,  1.28713121e+00],
       [-7.08833310e+00,  1.14642839e+00],
       [-7.06884341e+00,  1.00713245e+00],
       [-7.03925623e+00,  8.69795239e-01],
       [-6.99972199e+00,  7.34958055e-01],
       [-6.95049630e+00,  6.03127328e-01],
       [-6.89193652e+00,  4.74755877e-01],
       [-6.82437302e+00,  3.50284425e-01],
       [-6.74821525e+00,  2.30098399e-01],
       [-6.66390922e+00,  1.14535785e-01],
       [-6.57193335e+00,  3.88356228e-03],
       [-6.47278513e+00, -1.01618390e-01],
       [-6.36695670e+00, -2.01758968e-01],
       [-6.25498458e+00, -2.96398281e-01],
       [-6.13739482e+00, -3.85426231e-01],
       [-6.01471028e+00, -4.68763014e-01],
       [-5.88744824e+00, -5.46346656e-01],
       [-5.75613397e+00, -6.18127745e-01],
       [-5.62140720e+00, -6.84020261e-01],
       [-5.48433735e+00, -7.43454263e-01],
       [-5.34596508e+00, -7.96076215e-01],
       [-5.20690897e+00, -8.41754471e-01],
       [-5.06762350e+00, -8.80511770e-01],
       [-4.92846108e+00, -9.12447397e-01],
       [-4.78970182e+00, -9.37718410e-01],
       [-4.65157631e+00, -9.56468564e-01],
       [-4.51426216e+00, -9.68954868e-01],
       [-4.37791535e+00, -9.75343819e-01],
       [-4.24265441e+00, -9.75879225e-01],
       [-4.10857274e+00, -9.70808747e-01],
       [-3.97573275e+00, -9.60420277e-01],
       [-3.84415948e+00, -9.45060653e-01],
       [-3.71385262e+00, -9.25085313e-01],
       [-3.58478489e+00, -9.00870722e-01],
       [-3.45689622e+00, -8.72835518e-01],
       [-3.33010651e+00, -8.41400785e-01],
       [-3.20430203e+00, -8.07035656e-01],
       [-3.07856629e+00, -7.69887853e-01],
       [-2.95127137e+00, -7.36209186e-01],
       [-2.82316602e+00, -7.07132776e-01],
       [-2.69476420e+00, -6.83501196e-01],
       [-2.56636949e+00, -6.65904096e-01],
       [-2.43817688e+00, -6.54735626e-01],
       [-2.31033457e+00, -6.50221816e-01],
       [-2.18296910e+00, -6.52490151e-01],
       [-2.05618896e+00, -6.61560698e-01],
       [-1.93008387e+00, -6.77364257e-01],
       [-1.80472433e+00, -6.99760660e-01],
       [-1.68016534e+00, -7.28579270e-01],
       [-1.55643765e+00, -7.63553547e-01],
       [-1.43355219e+00, -8.04366369e-01],
       [-1.31149687e+00, -8.50628920e-01],
       [-1.19025206e+00, -9.01975644e-01],
       [-1.06977326e+00, -9.57947744e-01],
       [-9.49998760e-01, -1.01804088e+00],
       [-8.30859584e-01, -1.08175554e+00],
       [-7.12279616e-01, -1.14858816e+00],
       [-5.87733285e-01, -1.22187690e+00],
       [-4.62064280e-01, -1.29286981e+00],
       [-3.35173640e-01, -1.36132885e+00],
       [-2.06964469e-01, -1.42701603e+00],
       [-7.73527414e-02, -1.48971331e+00],
       [ 5.37337018e-02, -1.54921974e+00],
       [ 1.86354789e-01, -1.60535153e+00],
       [ 3.20556657e-01, -1.65794478e+00],
       [ 4.56347383e-01, -1.70691127e+00],
       [ 5.93728312e-01, -1.75216931e+00],
       [ 7.32682539e-01, -1.79366974e+00],
       [ 8.73174943e-01, -1.83139674e+00],
       [ 1.01514550e+00, -1.86538617e+00],
       [ 1.15850647e+00, -1.89573773e+00],
       [ 1.30316035e+00, -1.92257186e+00],
       [ 1.44899172e+00, -1.94605400e+00],
       [ 1.59587599e+00, -1.96637311e+00],
       [ 1.74367578e+00, -1.98375468e+00],
       [ 1.89225088e+00, -1.99842952e+00],
       [ 2.04144995e+00, -2.01066089e+00],
       [ 2.19111487e+00, -2.02073406e+00],
       [ 2.34108850e+00, -2.02892503e+00],
       [ 2.49122028e+00, -2.03552769e+00],
       [ 2.64141541e+00, -2.04083597e+00],
       [ 2.79164291e+00, -2.04513468e+00],
       [ 2.94189711e+00, -2.04839130e+00],
       [ 3.09217190e+00, -2.05056470e+00],
       [ 3.24246025e+00, -2.05161094e+00],
       [ 3.39275396e+00, -2.05148243e+00],
       [ 3.54304334e+00, -2.05012885e+00],
       [ 3.69331753e+00, -2.04749444e+00],
       [ 3.84356307e+00, -2.04351709e+00],
       [ 3.99376547e+00, -2.03813046e+00],
       [ 4.14390755e+00, -2.03125447e+00],
       [ 4.29396939e+00, -2.02280843e+00],
       [ 4.44392395e+00, -2.01262796e+00],
       [ 4.59370688e+00, -2.00023435e+00],
       [ 4.74320095e+00, -1.98499593e+00],
       [ 4.89221949e+00, -1.96629024e+00],
       [ 5.04049994e+00, -1.94350645e+00],
       [ 5.18769989e+00, -1.91604050e+00],
       [ 5.33341425e+00, -1.88335153e+00],
       [ 5.47718176e+00, -1.84494614e+00],
       [ 5.61850143e+00, -1.80040048e+00],
       [ 5.75686020e+00, -1.74939374e+00],
       [ 5.89173204e+00, -1.69167364e+00],
       [ 6.02260221e+00, -1.62708111e+00],
       [ 6.14897751e+00, -1.55554233e+00],
       [ 6.27038168e+00, -1.47704482e+00],
       [ 6.38638039e+00, -1.39165859e+00],
       [ 6.49650194e+00, -1.29943431e+00],
       [ 6.60030332e+00, -1.20049043e+00],
       [ 6.69735176e+00, -1.09498748e+00],
       [ 6.78721609e+00, -9.83122422e-01],
       [ 6.86948732e+00, -8.65148422e-01],
       [ 6.94365976e+00, -7.41295111e-01],
       [ 7.00923350e+00, -6.11871649e-01],
       [ 7.06557173e+00, -4.77205135e-01],
       [ 7.11197539e+00, -3.37746981e-01],
       [ 7.14766652e+00, -1.94138408e-01],
       [ 7.17180966e+00, -4.73278404e-02],
       [ 7.18362593e+00,  1.01313568e-01],
       [ 7.18259105e+00,  2.50072899e-01],
       [ 7.16847071e+00,  3.97195385e-01],
       [ 7.14133276e+00,  5.41082095e-01],
       [ 7.10149686e+00,  6.80331930e-01],
       [ 7.04944128e+00,  8.13708161e-01],
       [ 6.98587359e+00,  9.40191540e-01],
       [ 6.91163101e+00,  1.05897791e+00],
       [ 6.82757390e+00,  1.16942636e+00],
       [ 6.73458098e+00,  1.27105907e+00],
       [ 6.63353083e+00,  1.36355462e+00],
       [ 6.52526244e+00,  1.44670562e+00],
       [ 6.41063461e+00,  1.52050852e+00],
       [ 6.29044922e+00,  1.58507682e+00],
       [ 6.16544442e+00,  1.64061511e+00],
       [ 6.03631703e+00,  1.68745257e+00],
       [ 5.90372837e+00,  1.72606662e+00],
       [ 5.76827528e+00,  1.75701815e+00],
       [ 5.63048354e+00,  1.78091068e+00],
       [ 5.49083308e+00,  1.79844830e+00],
       [ 5.34974666e+00,  1.81039534e+00],
       [ 5.20759503e+00,  1.81758602e+00],
       [ 5.06469286e+00,  1.82088835e+00],
       [ 4.92137981e+00,  1.82121699e+00],
       [ 4.78031097e+00,  1.81955122e+00],
       [ 4.63931448e+00,  1.81892979e+00],
       [ 4.49830962e+00,  1.81948780e+00],
       [ 4.35728656e+00,  1.82135760e+00],
       [ 4.21623172e+00,  1.82467026e+00],
       [ 4.07512659e+00,  1.82954616e+00],
       [ 3.93394449e+00,  1.83611600e+00],
       [ 3.79264561e+00,  1.84451550e+00],
       [ 3.65116869e+00,  1.85487753e+00],
       [ 3.50941800e+00,  1.86733436e+00],
       [ 3.36725465e+00,  1.88201864e+00],
       [ 3.22453518e+00,  1.89906596e+00],
       [ 3.08129235e+00,  1.91859273e+00],
       [ 2.93798804e+00,  1.94064805e+00],
       [ 2.79519560e+00,  1.96523102e+00],
       [ 2.65319397e+00,  1.99236457e+00],
       [ 2.51204308e+00,  2.02209432e+00],
       [ 2.37174101e+00,  2.05447517e+00],
       [ 2.23228392e+00,  2.08956898e+00],
       [ 2.09367960e+00,  2.12745794e+00],
       [ 1.95594183e+00,  2.16822997e+00],
       [ 1.81909100e+00,  2.21198526e+00],
       [ 1.68315546e+00,  2.25884443e+00],
       [ 1.54816962e+00,  2.30894413e+00],
       [ 1.41417819e+00,  2.36245311e+00],
       [ 1.28123212e+00,  2.41955990e+00],
       [ 1.14938979e+00,  2.48047951e+00],
       [ 1.01873035e+00,  2.54550629e+00],
       [ 8.89358621e-01,  2.61503374e+00],
       [ 7.61512936e-01,  2.68948421e+00],
       [ 6.36170567e-01,  2.76882423e+00],
       [ 5.15034283e-01,  2.85239354e+00],
       [ 3.98771781e-01,  2.93997383e+00],
       [ 2.87640334e-01,  3.03152438e+00],
       [ 1.81769527e-01,  3.12702574e+00],
       [ 8.12606359e-02,  3.22645571e+00],
       [-1.37900142e-02,  3.32978512e+00],
       [-1.03348623e-01,  3.43693557e+00],
       [-1.87400416e-01,  3.54781377e+00],
       [-2.65923461e-01,  3.66233025e+00],
       [-3.38934577e-01,  3.78036989e+00],
       [-4.06464970e-01,  3.90180976e+00],
       [-4.68639722e-01,  4.02647318e+00],
       [-5.25568750e-01,  4.15419900e+00],
       [-5.77391729e-01,  4.28481451e+00],
       [-6.24280312e-01,  4.41813573e+00],
       [-6.66447067e-01,  4.55396451e+00],
       [-7.04069808e-01,  4.69212831e+00],
       [-7.37386136e-01,  4.83243078e+00],
       [-7.66614825e-01,  4.97469200e+00],
       [-7.91989693e-01,  5.11873045e+00],
       [-8.21133156e-01,  5.26216067e+00],
       [-8.55002596e-01,  5.40343267e+00],
       [-8.94629676e-01,  5.54187836e+00],
       [-9.40922856e-01,  5.67677652e+00],
       [-9.94621353e-01,  5.80736593e+00],
       [-1.05628599e+00,  5.93284619e+00],
       [-1.12633238e+00,  6.05235025e+00],
       [-1.20489293e+00,  6.16505251e+00],
       [-1.29198501e+00,  6.27005700e+00],
       [-1.38744118e+00,  6.36645348e+00],
       [-1.49091135e+00,  6.45333127e+00],
       [-1.60184278e+00,  6.52983420e+00],
       [-1.71949762e+00,  6.59519536e+00],
       [-1.84299034e+00,  6.64874839e+00],
       [-1.97129742e+00,  6.69001186e+00],
       [-2.10332197e+00,  6.71869122e+00],
       [-2.23794585e+00,  6.73469787e+00],
       [-2.37408647e+00,  6.73807123e+00],
       [-2.51071762e+00,  6.72904535e+00],
       [-2.64691052e+00,  6.70803915e+00],
       [-2.78184850e+00,  6.67552231e+00],
       [-2.91484058e+00,  6.63209824e+00],
       [-3.04533031e+00,  6.57845984e+00],
       [-3.17289199e+00,  6.51535167e+00],
       [-3.29722918e+00,  6.44356376e+00],
       [-3.41815562e+00,  6.36388918e+00],
       [-3.53561835e+00,  6.27718175e+00],
       [-3.64968070e+00,  6.18431151e+00],
       [-3.76051529e+00,  6.08615700e+00],
       [-3.86838781e+00,  5.98358573e+00],
       [-3.97366193e+00,  5.87746684e+00],
       [-4.07678100e+00,  5.76864770e+00],
       [-4.17825182e+00,  5.65793744e+00],
       [-4.27862751e+00,  5.54608917e+00],
       [-4.37852597e+00,  5.43379402e+00],
       [-4.47817492e+00,  5.32127762e+00],
       [-4.57760859e+00,  5.20857120e+00],
       [-4.67685056e+00,  5.09569550e+00],
       [-4.77592175e+00,  4.98267027e+00],
       [-4.87483358e+00,  4.86950493e+00],
       [-4.97359514e+00,  4.75620890e+00],
       [-5.07220793e+00,  4.64278293e+00],
       [-5.17066857e+00,  4.52922569e+00],
       [-5.26896334e+00,  4.41552448e+00],
       [-5.36707416e+00,  4.30166408e+00],
       [-5.46497488e+00,  4.18762338e+00],
       [-5.56263323e+00,  4.07337460e+00],
       [-5.66000295e+00,  3.95888042e+00]])



# static
# smoothed_central_line = None
smoothed_central_line = raceline_BaadalTrack
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

#-------------------------------------------------
# Codigo que al estar la Racing Line ... pasa a ser código muerto ...  

# 
# def smooth_central_line(center_line, max_offset, pp=0.10, p=0.05, c=0.70, n=0.05, nn=0.10, iterations=72, skip_step=1):
#     if max_offset < 0.0001:
#         return center_line
#     if skip_step < 1:
#         skip_step = 1
#     smoothed_line = center_line
#     for i in range(0, iterations):
#         smoothed_line = smooth_central_line_internal(center_line, max_offset, smoothed_line, pp, p, c, n, nn, skip_step)
#     return smoothed_line


# def smooth_central_line_internal(center_line, max_offset, smoothed_line, pp, p, c, n, nn, skip_step):
#     length = len(center_line)
#     new_line = [[0.0 for _ in range(2)] for _ in range(length)]
#     for i in range(0, length):
#         wpp = smoothed_line[(i - 2 * skip_step + length) % length]
#         wp = smoothed_line[(i - skip_step + length) % length]
#         wc = smoothed_line[i]
#         wn = smoothed_line[(i + skip_step) % length]
#         wnn = smoothed_line[(i + 2 * skip_step) % length]
#         new_line[i][0] = pp * wpp[0] + p * wp[0] + c * wc[0] + n * wn[0] + nn * wnn[0]
#         new_line[i][1] = pp * wpp[1] + p * wp[1] + c * wc[1] + n * wn[1] + nn * wnn[1]
#         while calc_distance(new_line[i], center_line[i]) >= max_offset:
#             new_line[i][0] = (0.98 * new_line[i][0]) + (0.02 * center_line[i][0])
#             new_line[i][1] = (0.98 * new_line[i][1]) + (0.02 * center_line[i][1])
#     return new_line


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

    # Es codigo muerto ahora ... 
    # if smoothed_central_line is None:
    #     max_offset = track_width * RACING_LINE_VS_CENTRAL_LINE * 0.5
    #     smoothed_central_line = smooth_central_line(waypoints, max_offset, skip_step=RACING_LINE_SMOOTHING_STEPS)
    #     print("track_waypoints:", "track_width =", track_width,
    #           "\ntrack_original =", waypoints, "\ntrack_smoothed =", smoothed_central_line)

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

    # PABLO IN_:
    # Hay un error que da por:
    #    "Typeerror: can only join an iterable"


    # print("rewards:" + (20 * "{:.4f}," + "{:.4f}").format(reward_total,
    #     wheels_off_track_penalty, reward_on_track, reward_exp_speed, reward_dir_steering, reward_prog_step,
    #     dislocation, track_direction_1, track_direction_2, track_direction_3, direction_diff_ratio,
    #     waypoints[wp_indices[0]][0], waypoints[wp_indices[0]][1], prev_point[0], prev_point[1],
    #     next_point_1[0], next_point_1[1], next_point_2[0], next_point_2[1], next_point_3[0], next_point_3[1]))

    previous_steps_reward = ema(previous_steps_reward, reward_total, 3)
    return float(0.0000001 + previous_steps_reward)
