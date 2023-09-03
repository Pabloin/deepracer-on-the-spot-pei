Model pei

----------------------------------------------------------------------------------
F02 es un Modelo entrenado desde cero .... 

    1) Discreto
    2) Waypoints
    3) Que no se mueva mucho ... 

    3) Que no se vaya de pusta

    ----

    4) No importa la velocidad



----------------------------------------------------------------------------------

La liga en Twitch

    https://www.twitch.tv/aws/clip/CuteRealFriseeAllenHuhu-94aCfSfGjC7DIR0h?lang=el



    s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F02/lgy-model-f02a/

----------------------------------------------------------------------------------

# sept 2023	Roger Super Raceway	60.17m	Clockwise  (2022_september_pro_cw)

DR_WORLD_NAME=2022_september_pro
DR_WORLD_NAME=2022_september_pro_cw

¿Cuál es?


-----------------------
Z01 con Waypoints


    ./create-spot-instance.sh     base lgy-model-f02a 120
    ./create-standard-instance.sh base lgy-model-f02a 120  
    
    ./create-standard-instance.sh base lgy-model-f02b  60 
    ./create-spot-instance.sh     base lgy-model-f02b  60


 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name lgy-model-f02b  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/LGY-Model-F02/lgy-model-f02b \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student

    
    s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F02/lgy-model-f02a/


aws s3 sync s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F02/ \
    .logsTmp/LGY-Model-F02/  

------------

s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F02/
s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F02/lgy-model-f02a/


aws s3 sync s3://base-bucket-1f3pfk38sjoqu/LGY-Model-F02/ \
    .logsTmp/LGY-Model-F02/  
    

aws s3 sync .logsTmp/LGY-Model-F02/  \
    s3://dr-models-glaciar-dots-std006/LGY-Model-F02/  \
    --profile voclabs/user2415006=Test_Student

---------------

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name lgy-model-f02a  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/LGY-Model-F02/lgy-model-f02a \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student







--------------------------

To win physical prizes, show us your skills by racing in one of the AWS monthly qualifiers, becoming a Pro by finishing in the top 10% of an Open race leaderboard, or