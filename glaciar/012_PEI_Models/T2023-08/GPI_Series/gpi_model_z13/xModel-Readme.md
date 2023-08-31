Model pei

-----------------------
Z01 con Waypoints


    ./create-spot-instance.sh base gpi-model-z01 60

    ./create-spot-instance.sh base gpi-model-z03g 360

    ./create-standard-instance.sh base gpi-model-z13a 480  



 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z13a  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/gpi_model_z03/DOTS-model-z13a \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z13a  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/gpi_model_z03/DOTS-model-z13a \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student

    
    s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/DOTS-model-z13a/


aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/ \
    .logsTmp/gpi_model_z03/  

------------

s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/
s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/DOTS-model-z13a/


aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/ \
    .logsTmp/gpi_model_z13/  
    
aws s3 sync .logsTmp/gpi_model_z13/  \
    s3://dr-models-glaciar-dots-std006/gpi_model_z13/  \
    --profile voclabs/user2415006=Test_Student

---------------

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z13aBis  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/gpi_model_z13/DOTS-model-z13a \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student