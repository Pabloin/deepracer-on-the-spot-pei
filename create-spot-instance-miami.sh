#!/bin/bash

set -xa

baseResourcesStackName=$1
shift

stackName=$1
shift

timeToLiveInMinutes=$1
shift

instanceTypeConfig=''

if [[ -n "$DEEPRACER_INSTANCE_TYPE" ]]; then
    instanceTypeConfig="InstanceType=$DEEPRACER_INSTANCE_TYPE"
fi
BUCKET=$(aws cloudformation describe-stacks --stack-name $baseResourcesStackName | jq '.Stacks | .[] | .Outputs | .[] | select(.OutputKey=="Bucket") | .OutputValue' | tr -d '"')


#amiId=$(aws ec2 describe-images --owners 747447086422 --filters "Name=state,Values=available" "Name=is-public,Values=true" --query 'sort_by(Images, &CreationDate)[-1].ImageId' | tr -d '"')
#amiId=$(aws ec2 describe-images --owners 845305768689 --filters "Name=state,Values=available" "Name=is-public,Values=true" --query 'sort_by(Images, &CreationDate)[-1].ImageId' | tr -d '"')
amiId=$(aws ec2 describe-images --owners 845305768689 --filters "Name=state,Values=available"                               --query 'sort_by(Images, &CreationDate)[-1].ImageId' | tr -d '"')

set +xa


echo "Africa Imagen: $amiId"
read -p "Esta Ok Africa? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

chmod +x ./validation.sh

./validation.sh

if [[ $? -ne 0 ]]; then
    while true; do
        echo -e "\e[1;33m  ##########  Error found in reward_function.py, want to continue anyway? \e[0m"
        read -p "[y / n]: " yn
        case $yn in
            [Yy]* ) break;;
            [Nn]* ) exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done
fi

set -x

CUSTOM_FILE_LOCATION=$(cat custom-files/run.env | grep DR_LOCAL_S3_CUSTOM_FILES_PREFIX= | awk -F'=' '{print $2}')
aws s3 cp custom-files s3://${BUCKET}/${CUSTOM_FILE_LOCATION} --recursive
aws cloudformation deploy --stack-name $stackName --parameter-overrides ${instanceTypeConfig} ResourcesStackName=$baseResourcesStackName TimeToLiveInMinutes=$timeToLiveInMinutes AmiId=$amiId BUCKET=$BUCKET CUSTOMFILELOCATION=$CUSTOM_FILE_LOCATION --template-file spot-instance.yaml --capabilities CAPABILITY_IAM
ASG=$(aws cloudformation describe-stacks --stack-name ${stackName} --query "Stacks[].Outputs[].OutputValue" --output text)
EC2_ID=$(aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names $ASG --query 'AutoScalingGroups[].Instances[].InstanceId' --output text)
EC2_IP=$(aws ec2 describe-instances --instance-ids ${EC2_ID} --query 'Reservations[].Instances[].PublicIpAddress[]' --output text)
echo "Logs will upload every 2 minutes to https://s3.console.aws.amazon.com/s3/buckets/${BUCKET}/${stackName}/logs/"
echo "Training should start shortly on ${EC2_IP}:8080"
echo "Once started, you should also be able to monitor training progress through ${EC2_IP}:8100/menu.html"
