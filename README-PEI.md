# deepracer-on-the-spot-pei


* run `git clone https://github.com/aws-deepracer-community/deepracer-on-the-spot-pei`
* run `cd deepracer-on-the-spot-pei`


*(11.111.11.11.1 my IP   )
MyIPAddress	181.164.84.94


3.87.87.207:8080 and 

http://3.87.87.207:8100/menu.html 

`./create-base-resources.sh base 11.111.11.11.1`
**This will run for around 3 minutes.**


`./create-spot-instance.sh base gpimodel-w00c 60`



#--------------------------------
    Why does ssh'ing to my EC2 instances take so long?
    Just put in your EC2's /etc/ssh/sshd_config:

    UseDNS no

    sudo systemctl restart systemd-logind 

#--------------------------------



                NOTE: 
                    using your own AMI will incur a charge of ~$1/day 
                    because an EC2 instance will be created daily to update the AMI.



                    US West (Oregon)
                    us-west-2

                    Africa (Cape Town)
                    af-south-1


ubuntu@ip-172-31-34-103:~/deepracer-on-the-spot-pei$ aws configure
AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [us-east-1]: af-south-1
Default output format [None]:

                    africa-base
                    CREATE_IN_PROGRESS	2023-08-29 12:04:34 UTC-0300	
                    Setup an EC2 instance for deep racer



                    Waiting for changeset to be created..
                    Waiting for stack create/update to complete
                    Successfully created/updated stack - africa-base
                    ubuntu@ip-172-31-34-103:~/deepracer-on-the-spot-pei$

                    lo siguiente es entrenar ... 

                    ./create-spot-instance.sh africa-base gpi-model-z03f-africa 120

                                        % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                                                        Dload  Upload   Total   Spent    Left  Speed
                                        100  144k    0  144k    0     0   605k      0 --:--:-- --:--:-- --:--:--  605k
                                        pretrained model DR_LOCAL_S3_PRETRAINED_PREFIX=gpi_model_z03/DOTS-model-z03e doesn't exist in africa-base-bucket-qxukn6l4iojx.
                                        ##########  Error found in reward_function.py, want to continue anyway?

                    ./create-spot-instance.sh base-africa gpi-model-z03f-africa 120

                            "The image ID 'null' is not valid. 
                            The expected format is ami-xxxxxxxx or ami-xxxxxxxxxxxxxxxxx. (Service: AmazonEC2; 
                            Status Code: 400; Error Code: InvalidAMIID.Malformed; 
                            
                            Request ID: 7fcffd02-ee33-49fa-adcd-0ededf21d485; Proxy: null)" 
                            (RequestToken: d2990da0-7f53-e364-a60a-a4485ee69fe1, HandlerErrorCode: GeneralServiceException)



./create-image-builder.sh base-africa

ubuntu@ip-172-31-34-103:~/deepracer-on-the-spot-pei/scripts$ ./create-image-builder.sh base-africa
+ resourcesStackName=base-africa
+ shift
+ stackName=
+ shift
+ aws cloudformation deploy --stack-name --template image-builder.yaml --capabilities CAPABILITY_IAM --parameter-overrides ResourcesStackName=base-africa

usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

aws: error: argument --stack-name: expected one argument

+ echo 'Image pipeline will run daily at midnight. 
    If you want to train a model now, go to '\''EC2 Image Builder'\'' 
    and run the pipeline manually by selecting actions > run pipeline. 
    This will take about 40 minutes to run fully. 
    You will know it is complete when the AMI is available in EC2 Console > AMIs'
    Image pipeline will run daily at midnight. 

    If you want to train a model now, go to 'EC2 Image Builder' 
    and run the pipeline manually by selecting actions > run pipeline. 
    This will take about 40 minutes to run fully. 
    You will know it is complete when the AMI is available in EC2 Console > AMIs



 ./create-image-builder.sh base-africa-rrrr  base-africa
+ resourcesStackName=base-africa-rrrr
+ shift
+ stackName=base-africa
+ shift
+ aws cloudformation deploy --stack-name base-africa --template image-builder.yaml --capabilities CAPABILITY_IAM --parameter-overrides ResourcesStackName=base-africa-rrrr

Waiting for changeset to be created..




-------------------------


                            
        ./create-base-resources.sh  africa-base   181.164.84.94

                If you wish to run your own AMI, 
                    or run in a region other than us-east-1, 

                use ./create-image-builder.sh 
                    to create the daily refreshing pipeline 
                    and update your spot/standard instance bash scripts to use your AMI. 




ubuntu@ip-172-31-34-103:~$ $(aws ec2 describe-images --owners 747447086422 --filters "Name=state,Values=available" "Name=is-public,Values=true" --query 'sort_by(Images, &CreationDate)[-1].ImageId' | tr -d '"')

ami-027fc0bd0d2474c65:



aws ec2 copy-image \
    --region af-south-1 \
    --name ami-dr-dots \
    --source-region us-east-1 \
    --source-image-id ami-027fc0bd0d2474c65 \
    --description "La copya de AMI DOTS para Africa."

    An error occurred (InvalidRequest) when calling the CopyImage operation: 
    You do not have permission to access the storage of this ami


aws ec2 describe-images --image-id ami-027fc0bd0d2474c65  --region us-east-1  --query 'Images[0].OwnerId'



----------------------------------------------------------------------------------------------------------

ubuntu@ip-172-31-34-103:~$ aws ec2 describe-images --image-id ami-027fc0bd0d2474c65  --region us-east-1
{
    "Images": [
        {
            "Architecture": "x86_64",
            "CreationDate": "2023-08-21T00:25:38.000Z",
            "ImageId": "ami-027fc0bd0d2474c65",
            "ImageLocation": "747447086422/UbuntuServerForDeepRacer-imagesource 2023-08-21T00-00-16.394153Z",
            "ImageType": "machine",
            "Public": true,
            "OwnerId": "747447086422",
            "PlatformDetails": "Linux/UNIX",
            "UsageOperation": "RunInstances",
            "State": "available",
            "BlockDeviceMappings": [
                {
                    "DeviceName": "/dev/sda1",
                    "Ebs": {
                        "DeleteOnTermination": true,
                        "SnapshotId": "snap-0c0a2fc67f8cb68ce",
                        "VolumeSize": 40,
                        "VolumeType": "gp2",
                        "Encrypted": false
                    }
                },
                {
                    "DeviceName": "/dev/sdb",
                    "VirtualName": "ephemeral0"
                },
                {
                    "DeviceName": "/dev/sdc",
                    "VirtualName": "ephemeral1"
                }
            ],
            "EnaSupport": true,
            "Hypervisor": "xen",
            "Name": "UbuntuServerForDeepRacer-imagesource 2023-08-21T00-00-16.394153Z",
            "RootDeviceName": "/dev/sda1",
            "RootDeviceType": "ebs",
            "SriovNetSupport": "simple",
            "VirtualizationType": "hvm",
            "DeprecationTime": "2025-08-21T00:25:38.000Z"
        }
    ]
}



        ./create-base-resources.sh  base-africa   181.164.84.94

        ./create-base-resources.sh  deepracer-africa-dots   181.164.84.94




*******************
AFRICA de nuevo:

    3/9/2023

    If you wish to run your own AMI, or run in a region other than us-east-1, 
    use ./create-image-builder.sh to create the daily refreshing pipeline and update 
    your spot/standard instance bash scripts to use your AMI.



aws cloudformation deploy \
       --stack-name $stackName  \
       --template image-builder-africa.yaml  \
       --capabilities CAPABILITY_IAM  \
       --parameter-overrides ResourcesStackName=$resourcesStackName    \
       --region af-south-1 


./create-image-builder-africa.sh deepracer-ami-africa  base-africa



aws cloudformation update-stack 
       --region YOUR_REGION 
       --template-body file://YOUR_TEMPLATE_FILE_TAGS_COMMENTED 
       —stack-name YOUR_STACK_NAME















Timestamp
Logical ID
Status
Status reason
Timestamp
Logical ID
Status
Status reason
2023-09-04 01:32:16 UTC-0300	deepracer-africa-dots	
DELETE_COMPLETE
-
2023-09-04 01:32:14 UTC-0300	deepracer-africa-dots	
DELETE_IN_PROGRESS
User Initiated


2023-09-03 04:54:31 UTC-0300	deepracer-africa-dots	
ROLLBACK_COMPLETE
-


2023-09-03 04:54:30 UTC-0300	InterruptionNotification	
DELETE_COMPLETE
-


2023-09-03 04:54:15 UTC-0300	EFS	
DELETE_COMPLETE
-


2023-09-03 04:52:07 UTC-0300	Bucket	
DELETE_COMPLETE
-


2023-09-03 04:52:07 UTC-0300	NACLEntry	
DELETE_COMPLETE
-


2023-09-03 04:52:07 UTC-0300	TerminationLambdaRole	
DELETE_COMPLETE
-


2023-09-03 04:52:07 UTC-0300	SecurityGroup	
DELETE_COMPLETE
-


2023-09-03 04:52:07 UTC-0300	Bucket	
DELETE_IN_PROGRESS
-


2023-09-03 04:52:07 UTC-0300	InstanceRole	
DELETE_COMPLETE
-


2023-09-03 04:52:07 UTC-0300	FutureTimeCronExpressionLambdaRole	
DELETE_COMPLETE
-


2023-09-03 04:52:04 UTC-0300	deepracer-africa-dots	
ROLLBACK_IN_PROGRESS
The following resource(s) failed to create: [InstanceRole, FutureTimeCronExpressionLambdaRole, InterruptionNotification, Bucket, TerminationLambdaRole, NACLEntry, EFS, SecurityGroup]. Rollback requested by user.


2023-09-03 04:52:04 UTC-0300	Bucket	
CREATE_FAILED
Resource creation cancelled


2023-09-03 04:52:03 UTC-0300	InstanceRole	
CREATE_FAILED
API: iam:CreateRole User: arn:aws:sts::845305768689:assumed-role/DeepRacerRole/i-031e1c3f26b40a8f7 is not authorized to perform: iam:CreateRole on resource: arn:aws:iam::845305768689:role/deepracer-africa-dots-InstanceRole-12W0I7649LJB6 because no identity-based policy allows the iam:CreateRole action


2023-09-03 04:52:03 UTC-0300	FutureTimeCronExpressionLambdaRole	
CREATE_FAILED
API: iam:CreateRole User: arn:aws:sts::845305768689:assumed-role/DeepRacerRole/i-031e1c3f26b40a8f7 is not authorized to perform: iam:CreateRole on resource: arn:aws:iam::845305768689:role/deepracer-africa-dots-FutureTimeCronExpressionLamb-15VC2890L2Z6W because no identity-based policy allows the iam:CreateRole action


2023-09-03 04:52:03 UTC-0300	EFS	
CREATE_FAILED
Resource creation cancelled


2023-09-03 04:52:03 UTC-0300	TerminationLambdaRole	
CREATE_FAILED
API: iam:CreateRole User: arn:aws:sts::845305768689:assumed-role/DeepRacerRole/i-031e1c3f26b40a8f7 is not authorized to perform: iam:CreateRole on resource: arn:aws:iam::845305768689:role/deepracer-africa-dots-TerminationLambdaRole-1OYM3QSVR18ZL because no identity-based policy allows the iam:CreateRole action


2023-09-03 04:52:03 UTC-0300	InterruptionNotification	
CREATE_FAILED
Resource creation cancelled


2023-09-03 04:52:03 UTC-0300	InstanceRole	
CREATE_IN_PROGRESS
Did not have IAM permissions to process tags on AWS::IAM::Role resource.


2023-09-03 04:52:03 UTC-0300	NACLEntry	
CREATE_FAILED
API: ec2:CreateNetworkAclEntry You are not authorized to perform this operation. Encoded authorization failure message: xSZnBYVLyOqdw9wPWrhQIuDOjMzSjzu0PAKUlaHhU97ZlcXC_Xp5uqThSVjLzTw3H_x3-TgAlcvhYrdIEFbUTQWPFMIisG2B7A2txo88Sw4e2LKTMa8LmkQsiRXhMxlPnq5jVX-PihJwbISSvVb3DRoCPN1ywM1wd4bgxpk5gGd0Y8ako2CXIcT_49-zygynS0DZSBvtfmObUbLJ79-3SVbvL9F922C8RRpIHppAuwTpYtx1u1pC4VWCgW0KQ-Z07ftazfbc43_T1BH6WtnDhv_Y9wqH0DlJdo2I5f5H5zr-HZbGogRuqG9os12KMn-RUhzi90vbV2h7t0-P8-6n2DGyOQle2JU73Oc_ZkdtxSUV1qoDJid4Weskv_Ha2OoOs44raOLyr_gUft0XYWbG62a5VqGsgyfzO6vc6bs21dh03RDHq0fkuKjPRG8uXDEUrtcKTcaPpq3zJ3F9re3E2W93imSokfDc9BrisSjkuQJPO9lO--iDN3Nb_uJjfVBQjF3-hyHI9WcZ-2mfmKwnIPY5_fn9dFd_uhgG3jDdfhTXLrSIl5QMPnI26J8Dx5WZ4MpGiX172rmrJtrHQGR8cmvvIvVM8nHr1Gkjsu6Q0opuvNSbuCwghhk5


2023-09-03 04:52:03 UTC-0300	FutureTimeCronExpressionLambdaRole	
CREATE_IN_PROGRESS
Did not have IAM permissions to process tags on AWS::IAM::Role resource.


2023-09-03 04:52:03 UTC-0300	TerminationLambdaRole	
CREATE_IN_PROGRESS
Did not have IAM permissions to process tags on AWS::IAM::Role resource.


2023-09-03 04:52:03 UTC-0300	SecurityGroup	
CREATE_FAILED
API: ec2:CreateSecurityGroup You are not authorized to perform this operation. Encoded authorization failure message: kOXkBBNz-KLtwqG1i1945Qa9NLCGeLcm7EEB1iHtn_mo9iwzrgRoDQa5964Fn0D9qSB7gizA9gk7wOMBam8a3xNkYy061MlrJLPY9xrG-UIN7DbNuTbUp4ZJ5QLDlQyOb2A2F5PcZVeGPU8cb-W7_ueAIaLRpLSbSx5b5RTuVnBYXDA_Xk-I_S8EftnlM2fO0v4Qx59nlo7hpPy_z5me84NmwA7CGyEHWeolaGrlZYs-yevLJOuN4hI7z5OPe9UZl5OXQIt6NRxGkWSREkMbOXUvIiQCGey7lNRjQwP-y4-M2uIaGUP2HHb2I2U3BU7qT_RwhJUuHzFlpavg45rcDjlfnVrQkZVKyTdOcc6vE7TPVgbXHvAuDXwWPPqgSMs8WEz9ydZQpZt0BKpOYbyy4aqgRPOLF4oz5agkDafBWnjcFGmVnPbJnEsO_qXAJ6PosGzAvtDyJHi4rUq0DtCO7jDBKssbeBCbWFO1AZQA7jDG4gZJ-C3v7mYDdBdWZDeNZpRZRpVYXNwFbRGwjs9CVE8_1Peie9D_jh-g3E1F5_c58CHXSQ


2023-09-03 04:52:02 UTC-0300	NACLEntry	
CREATE_IN_PROGRESS
-


2023-09-03 04:52:02 UTC-0300	InstanceRole	
CREATE_IN_PROGRESS
-


2023-09-03 04:52:02 UTC-0300	InterruptionNotification	
CREATE_IN_PROGRESS
-


2023-09-03 04:52:02 UTC-0300	FutureTimeCronExpressionLambdaRole	
CREATE_IN_PROGRESS
-


2023-09-03 04:52:02 UTC-0300	EFS	
CREATE_IN_PROGRESS
-


2023-09-03 04:52:02 UTC-0300	Bucket	
CREATE_IN_PROGRESS
-


2023-09-03 04:52:02 UTC-0300	SecurityGroup	
CREATE_IN_PROGRESS
-


2023-09-03 04:52:02 UTC-0300	TerminationLambdaRole	
CREATE_IN_PROGRESS
-


2023-09-03 04:51:59 UTC-0300	deepracer-africa-dots	
CREATE_IN_PROGRESS
User Initiated


2023-09-03 04:51:54 UTC-0300	deepracer-africa-dots	
REVIEW_IN_PROGRESS
User Initiated
