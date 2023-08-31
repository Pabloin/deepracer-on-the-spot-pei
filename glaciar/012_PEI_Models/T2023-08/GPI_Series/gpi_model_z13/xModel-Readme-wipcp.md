Es para Spot



    ./create-standard-instance.sh base gpi-model-z13a 480  

    

a las 3:22

.... 8 horas ...  480 minutos ... 6 workers de GPU ... ¿Debería Servir ... ?



upload: custom-files/model_metadata.json to s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/custom_files/model_metadata.json
upload: custom-files/reward_function.py to s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/custom_files/reward_function.py
upload: custom-files/__pycache__/reward_function.cpython-37.pyc to s3://base-bucket-1f3pfk38sjoqu/gpi_model_z13/custom_files/__pycache__/reward_function.cpython-37.pyc
+ aws cloudformation deploy --stack-name gpi-model-z13a --parameter-overrides ResourcesStackName=base TimeToLiveInMinutes=480 AmiId=ami-027fc0bd0d2474c65 BUCKET=base-bucket-1f3pfk38sjoqu CUSTOMFILELOCATION=gpi_model_z13/custom_files --template-file standard-instance.yaml

Waiting for changeset to be created..
Waiting for stack create/update to complete
Successfully created/updated stack - gpi-model-z13a
++ aws cloudformation list-exports --query 'Exports[?Name=='\''gpi-model-z13a-PublicIp'\''].Value' --no-paginate --output text
+ EC2_IP=3.238.98.10
+ echo 'Logs will upload every 2 minutes to https://s3.console.aws.amazon.com/s3/buckets/base-bucket-1f3pfk38sjoqu/gpi-model-z13a/logs/'
Logs will upload every 2 minutes to https://s3.console.aws.amazon.com/s3/buckets/base-bucket-1f3pfk38sjoqu/gpi-model-z13a/logs/
+ echo 'Training should start shortly on 3.238.98.10:8080'
Training should start shortly on 3.238.98.10:8080
+ echo 'Once started, you should also be able to monitor training progress through 3.238.98.10:8100/menu.html'
Once started, you should also be able to monitor training progress through 3.238.98.10:8100/menu.html
ubuntu@ip-172-31-34-103:~/deepracer-on-the-spot-pei$
