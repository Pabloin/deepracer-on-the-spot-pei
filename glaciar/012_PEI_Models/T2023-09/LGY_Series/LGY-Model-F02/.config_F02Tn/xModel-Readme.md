Empieza en zero

    La serie T es la tesis pura y dura ... a lo sumo con mas logs activos


    ./create-spot-instance.sh        base        lgy-model-f02TAa  120     (wip)
    ./create-spot-instance-africa.sh base-africa lgy-model-f02TAa  360     (wip)

    ./create-spot-instance.sh     base lgy-model-f02Ta  120   (...)
    
    ./create-standard-instance.sh base lgy-model-f02Tc  120   (WIP)  


    ./create-spot-instance.sh     base lgy-model-f02Tc  60




    ./create-spot-instance-africa.sh     base lgy-model-f02TaAfrica  360  africa (...)



al fimal -...

    no me habpian aprobado la cota. ..


   aws imagebuilder start-image-pipeline-execution  --image-pipeline-arn arn:aws:imagebuilder:af-south-1:845305768689:image-pipeline/deepracerimagebuildpipeline-base-africa-ami


///---------------------

    base-africa-AMIParameter

    ./create-image-builder-africa.sh  base-africa  deepracer-ami-africa
    No export named deepracer-ami-africa-AMIParameter found

    ./create-image-builder-africa.sh  base-africa  base-africa
    Cannot import base-africa-Bucket while it is being processed by exporting stack base-africa

    ./create-image-builder-africa.sh  base-africa-ami  base-africa
    No export named base-africa-ami-Region found


    ./create-image-builder-africa.sh  base-africa  base-africa
    Cannot import base-africa-Bucket while it is being processed by exporting stack base-africa


    ./create-image-builder-africa.sh deepracer-ami-africa  base-africa
    No export named deepracer-ami-africa-SecurityGroup found

    antes:
    (en teoria...)
    # ./create-image-builder-africa.sh  base-africa  deepracer-ami-africa 

***********************


    ./create-image-builder-africa.sh deepracer-ami-africa  base-africa
                     No export named deepracer-ami-africa-SecurityGroup found
    
                                             base-africa-SecurityGroup-LFEYJ2MYRV53 


***********************    
Empiezo de cero otra vez

    ./create-base-resources.sh  base-africa   181.164.84.94


    ./create-image-builder-africa.sh base-africa  base-africa-ami   (WIP)


        PArece que anduvo todo Ok ... 



        ubuntu@ip-172-31-1-160:~/deepracer-on-the-spot-pei$




                ubuntu@ip-172-31-1-160:~/deepracer-on-the-spot-pei$
                ubuntu@ip-172-31-1-160:~/deepracer-on-the-spot-pei$ ./create-base-resources.sh  base-africa   181.164.84.94
                + stackName=base-africa
                + shift
                + ip=181.164.84.94
                + shift
                ++ generate_rule_number
                +++ aws ec2 describe-network-acls
                +++ tr -d ' '
                +++ grep RuleNumber
                +++ awk -F : '{ print $2 }'
                +++ sort -u
                ++ existing_rule_numbers='100
                32767'
                +++ shuf -i 1-32000 -n 1
                ++ rule_number_candidate=31735
                +++ echo 100 32767
                +++ grep -xc 31735
                +++ tr ' ' '\n'
                ++ [[ 0 -ne 0 ]]
                ++ echo 31735
                + ruleN=31735
                + [[ base-africa == '' ]]
                + [[ 181.164.84.94 == '' ]]
                + [[ 31735 == '' ]]
                + subnetsConfig=
                ++ aws ec2 describe-vpcs --filters Name=isDefault,Values=true --query 'Vpcs[*].VpcId' --output text
                + vpc=vpc-02ea9461150a96041
                ++ aws ec2 describe-subnets --filters Name=vpc-id,Values=vpc-02ea9461150a96041 --query 'Subnets[*].SubnetId'
                ++ grep subnet
                ++ wc -l
                + subnetCount=3
                + index=0
                + [[ 0 -lt 3 ]]
                ++ aws ec2 describe-subnets --filters Name=vpc-id,Values=vpc-02ea9461150a96041 --query 'Subnets[0].SubnetId' --output text
                + subnetId=subnet-07dcb28f13f375b2c
                + subnetsConfig=' Subnet0=subnet-07dcb28f13f375b2c'
                ++ expr 0 + 1
                + index=1
                + [[ 1 -lt 3 ]]
                ++ aws ec2 describe-subnets --filters Name=vpc-id,Values=vpc-02ea9461150a96041 --query 'Subnets[1].SubnetId' --output text
                + subnetId=subnet-01705003e08f53278
                + subnetsConfig=' Subnet0=subnet-07dcb28f13f375b2c Subnet1=subnet-01705003e08f53278'
                ++ expr 1 + 1
                + index=2
                + [[ 2 -lt 3 ]]
                ++ aws ec2 describe-subnets --filters Name=vpc-id,Values=vpc-02ea9461150a96041 --query 'Subnets[2].SubnetId' --output text
                + subnetId=subnet-02e6e811d730fac58
                + subnetsConfig=' Subnet0=subnet-07dcb28f13f375b2c Subnet1=subnet-01705003e08f53278 Subnet2=subnet-02e6e811d730fac58'
                ++ expr 2 + 1
                + index=3
                + [[ 3 -lt 3 ]]
                ++ aws ec2 describe-network-acls --filters Name=vpc-id,Values=vpc-02ea9461150a96041 --query 'NetworkAcls[*].NetworkAclId' --output text
                + nacl=acl-09afd36d166c069c7
                + aws cloudformation deploy --template ./base-resources.yaml --stack-name base-africa --parameter-overrides Subnet0=subnet-07dcb28f13f375b2c Subnet1=subnet-01705003e08f53278 Subnet2=subnet-02e6e811d730fac58 VPC=vpc-02ea9461150a96041 MyIPAddress=181.164.84.94 NetworkAclId=acl-09afd36d166c069c7 RuleNumber=31735 --capabilities CAPABILITY_IAM

                Waiting for changeset to be created..
                Waiting for stack create/update to complete



                Successfully created/updated stack - base-africa
                ubuntu@ip-172-31-1-160:~/deepracer-on-the-spot-pei$

                ubuntu@ip-172-31-1-160:~/deepracer-on-the-spot-pei/scripts$
                ubuntu@ip-172-31-1-160:~/deepracer-on-the-spot-pei/scripts$ ./create-image-builder-africa.sh base-africa  base-africa-ami
                + resourcesStackName=base-africa
                + shift
                + stackName=base-africa-ami
                + shift
                + aws cloudformation deploy --stack-name base-africa-ami --template image-builder-africa.yaml --capabilities CAPABILITY_IAM --parameter-overrides ResourcesStackName=base-africa

                Waiting for changeset to be created..
                Waiting for stack create/update to complete



Successfully created/updated stack - base-africa-ami
Image pipeline will run daily at midnight.

If you want to train a model now, go to 'EC2 Image Builder' and
run the pipeline manually by selecting actions > run pipeline.
This will take about 40 minutes to run fully.
You will know it is complete when the AMI is available in EC2 Console > AMIs

ubuntu@ip-172-31-1-160:~/deepracer-on-the-spot-pei/scripts$


