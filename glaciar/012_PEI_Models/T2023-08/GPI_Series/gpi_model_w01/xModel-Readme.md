Model pei

-----------------------
Entrenado?



-----------------------
-- Actualizar ~/ 

cp ~/deepracer-on-the-spot-pei/glaciar/012_PEI_Models/GPI_Series/gpi_model_w01  \
   ~/deepracer-on-the-spot-pei/custom-files

---------------------
SPOT

   https://github.com/aws-deepracer-community/deepracer-on-the-spot


---------------------
DOCS

   https://github.com/aws-deepracer-community/deepracer-race-data/blob/main/raw_data/tracks/README.md

   https://github.com/oscarYCL/deepracer-waypoints-workshop/tree/main/Waypoint%20Map


   And traks en K1999
   https://github.com/dp770/aws_deepracer_worksheet/tree/main/tracks


----------------
Esto esta en WIP






-------------------------
Respecto a w00d

   Agrego
   Siguiendo a 
   https://blog.gofynd.com/how-we-broke-into-the-top-1-of-the-aws-deepracer-virtual-circuit-573ba46c275

   How we broke into the top 1% of the AWS DeepRacer Virtual Circuit
   
   We found that tracks which contained sharp hair-pin bends could be traversed using the lowest speed of about 1.25 m/s. For the Albert track, (i.e. August 2020 virtual circuit), we found this speed to be 2 m/s. For most tracks a maximum turning angle of 30 degrees was found to be sufficient. For the Albert track, we threw in an additional action with a 45 degree turning angle to help the car make sharper right turns. We set the maximum speed of the model to 4 m/s. We found this speed to be high enough to allow the car to go fast without losing control. We then further divided the speed and turning intervals to obtain the following model_metadata.json
   

   {
   "action_space": [
   { "steering_angle": -45, "speed": 2.00},
   { "steering_angle": -30, "speed": 2.00},
   { "steering_angle": -20, "speed": 2.50},
   { "steering_angle": -10, "speed": 3.30},
   { "steering_angle": -10, "speed": 3.70},
   { "steering_angle": 0,   "speed": 4.0},
   { "steering_angle": 0,   "speed": 3.70},
   { "steering_angle": 0,   "speed": 3.30},
   { "steering_angle": 0,   "speed": 3.00},
   { "steering_angle": 0,   "speed": 2.75},
   { "steering_angle": 0,   "speed": 2.50},
   { "steering_angle": 0,   "speed": 2.25},
   { "steering_angle": 0,   "speed": 2.00},
   { "steering_angle": 10,  "speed": 3.70},
   { "steering_angle": 10,  "speed": 3.30},
   { "steering_angle": 20,  "speed": 2.50},
   { "steering_angle": 30,  "speed": 2.00}],
   "sensor": ["FRONT_FACING_CAMERA"],
   "neural_network": "DEEP_CONVOLUTIONAL_NETWORK_SHALLOW"
   }


   -------------------------
Respecto a w01

   - Saco el SAC
   - Arreglo los hiperparametros a algo coherente o que conozco

     "action_space": {
         "steering_angle": {
            "high": 25.0,
            "low": -25.0
         },
         "speed": {
            "high": 3.0,
            "low":  0.7
         }
      }, 