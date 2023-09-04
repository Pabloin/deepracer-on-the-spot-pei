#!/bin/bash

set -x

resourcesStackName=$1
shift

stackName=$1
shift


aws cloudformation deploy \
       --stack-name $stackName  \
       --template image-builder-africa.yaml  \
       --capabilities CAPABILITY_IAM  \
       --parameter-overrides ResourcesStackName=$resourcesStackName  \
       --role-arn arn:aws:iam::845305768689:role/DeepRacerDOT


# aws cloudformation deploy \
#        --stack-name base-africa-ami \
#        --template image-builder-africa.yaml  \
#        --capabilities CAPABILITY_IAM  \
#        --parameter-overrides ResourcesStackName=base-africa


# ./create-image-builder-africa.sh deepracer-ami-africa  base-africa


# aws cloudformation deploy --stack-name $stackName --template image-builder-africa.yaml --capabilities CAPABILITY_IAM --parameter-overrides ResourcesStackName=$resourcesStackName

echo "Image pipeline will run daily at midnight. "
echo "If you want to train a model now, go to 'EC2 Image Builder' and "
echo "   run the pipeline manually by selecting actions > run pipeline. " 
echo "   This will take about 40 minutes to run fully. "
echo "   You will know it is complete when the AMI is available in EC2 Console > AMIs"
