#
#       ./create-spot-instance.sh base aws-track-c01        60      (2022_july_pro_cw) 












https://github.com/aws-deepracer-community/deepracer-race-data/blob/main/raw_data/tracks/README.md



#       ./create-spot-instance.sh base aws-beast-b01        60      (2022_september_pro)
#       ./create-spot-instance.sh base aws-track-c01b       60      (Spain_track) 
#       ./create-spot-instance.sh base aws-track-c01c       60      (caecer_gp)
#       ./create-spot-instance.sh base aws-track-c01d       60      (2022_august_pro_cw)



2022_april_pro_cw
Speedway	2022-04-01T00:00:00Z	2022_april_pro.npy 2022_april_pro_ccw.npy 2022_april_pro_cw.npy	67.46 meters	1.07 meters



arctic_pro_cw
Hot Rod Super Speedway	2021-07-31T00:00:01Z	arctic_pro.npy arctic_pro_cw.npy arctic_pro_ccw.npy	59.50 meters	0.01 meters

dubai_pro
Baja Highway	2021-06-30T16:58:00Z	dubai_pro.npy	64.67 meters	0.01 meters

2022_march_pro_cw
Rogue Raceway	2022-03-01T00:00:00Z	2022_march_pro_ccw.npy 2022_march_pro.npy 2022_march_pro_cw.npy	76.76 meters	1.07 meters


2022_august_pro_cw
Jochem Highway	2022-08-01T00:00:00Z	2022_august_pro_ccw.npy 2022_august_pro.npy 2022_august_pro_cw.npy	63.88 meters	1.07 meters



caecer_gp
Vivalas Speedway	2021-10-30T00:00:00Z	caecer_gp.npy	73.78 meters	1.08 meters


Spain_track
Circuit de Barcelona-Catalunya	2020-05-01T00:00:00Z	Spain_track.npy	60.00 meters	1.07 meter


2022_july_pro_cw
DBro Super Raceway	2022-07-01T00:00:00Z	2022_july_pro_ccw.npy 2022_july_pro.npy 2022_july_pro_cw.npy	57.89 meters	1.07 meters



# sept 2023	Roger Super Raceway	60.17m	Clockwise  (2022_september_pro_cw)
#
#
#       ./create-spot-instance.sh base aws-beast-b01       60    (2022_september_pro)
#       ./create-spot-instance.sh base aws-track-c01       60    (2022_july_pro_cw)
#       ./create-spot-instance.sh base aws-track-c01b      60    (Spain_track) 











*******************************************
Serie P01 es la del Vector y Continuo





##
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


Pure pursiot
https://scholar.sun.ac.za/server/api/core/bitstreams/e4d5a9a2-66ac-4829-ac8a-2bc6bab97485/content