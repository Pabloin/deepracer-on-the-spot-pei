Model pei

----------------------------------------------------------------------------------

    DR_LOCAL_S3_PRETRAINED_PREFIX=LGY-Model-F01/lgy-model-f01c
    DR_LOCAL_S3_PRETRAINED=True

    DR_LOCAL_S3_CUSTOM_FILES_PREFIX=LGY-Model-F01/custom_files
    DR_LOCAL_S3_MODEL_PREFIX=LGY-Model-F01/lgy-model-f01a


----------------------------------------------------------------------------------

La liga en Twitch

    https://www.twitch.tv/aws/clip/CuteRealFriseeAllenHuhu-94aCfSfGjC7DIR0h?lang=el



    s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F01/lgy-model-f01a/

----------------------------------------------------------------------------------

# sept 2023	Roger Super Raceway	60.17m	Clockwise  (2022_september_pro_cw)

DR_WORLD_NAME=2022_september_pro
DR_WORLD_NAME=2022_september_pro_cw

¿Cuál es?


-----------------------
Z01 con Waypoints


    ./create-spot-instance.sh     base lgy-model-f01a  60
    ./create-standard-instance.sh base lgy-model-f01a 120  
    
    ./create-standard-instance.sh base lgy-model-f01b 240 


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

    
    s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F01/lgy-model-f01a/


aws s3 sync s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F01/ \
    .logsTmp/LGY-Model-F01/  

------------

s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F01/
s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F01/lgy-model-f01a/


aws s3 sync s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F01/ \
    .logsTmp/LGY-Model-F01/  
    

aws s3 sync .logsTmp/LGY-Model-F01/  \
    s3://dr-models-glaciar-dots-std006/LGY-Model-F01/  \
    --profile voclabs/user2415006=Test_Student

---------------

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name lgy-model-f01a  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/LGY-Model-F01/lgy-model-f01a \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student







--------------------------

To win physical prizes, show us your skills by racing in one of the AWS monthly qualifiers, becoming a Pro by finishing in the top 10% of an Open race leaderboard, or