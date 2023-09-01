Model pei

----------------------------------------------------------------------------------

    DR_LOCAL_S3_PRETRAINED_PREFIX=gpi_model_z13/lgy-model-f01c
    DR_LOCAL_S3_PRETRAINED=True

    DR_LOCAL_S3_CUSTOM_FILES_PREFIX=LGY-Model-F01/custom_files
    DR_LOCAL_S3_MODEL_PREFIX=LGY-Model-F01/lgy-model-f01a


----------------------------------------------------------------------------------

# sept 2023	Roger Super Raceway	60.17m	Clockwise  (2022_september_pro_cw)

DR_WORLD_NAME=2022_september_pro
DR_WORLD_NAME=2022_september_pro_cw

¿Cuál es?


-----------------------
Z01 con Waypoints


    ./create-spot-instance.sh     base lgy-model-f01a  60
    ./create-standard-instance.sh base lgy-model-f01a 480  



 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name lgy-model-f01a  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/LGY-Model-F01/lgy-model-f01a \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name lgy-model-f01a  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/LGY-Model-F01/lgy-model-f01a \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student

    
    s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/lgy-model-f01a/


aws s3 sync s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F01/ \
    .logsTmp/LGY-Model-F01/  

------------

s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/
s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/lgy-model-f01a/


aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/ \
    .logsTmp/gpi_model_z13/  
    
aws s3 sync .logsTmp/gpi_model_z13/  \
    s3://dr-models-glaciar-dots-std006/gpi_model_z13/  \
    --profile voclabs/user2415006=Test_Student

---------------

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name lgy-model-f01aBis  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/gpi_model_z13/lgy-model-f01a \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student






