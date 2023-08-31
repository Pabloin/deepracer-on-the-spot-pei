Readme WIP Copy Paste



[WIP-UCEMA...]
    AWS Academy Learner Lab [40078] (Ucema)
    Used $0.0 of $100
    Used $42.41 of $100

    arn:aws:iam::764531084004:role/LabRole
    voclabs/user2415006=Test_Student

aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/ \
    .logsTmp/gpi_model_z03/  
    

# WINDOWS
aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/  .logsTmp/gpi_model_z03/  
    

aws s3 sync .logsTmp/gpi_model_z03/  \
    s3://dr-models-glaciar-dots-std006/gpi_model_z03/  \
    --profile voclabs/user2415006=Test_Student

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z03gEC2  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/gpi_model_z03/DOTS-model-z03g \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student


 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z03gEC2-CCW  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/gpi_model_z03/DOTS-model-z03g \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student



------------------

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z03cCCW  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std006/gpi_model_z03/DOTS-model-z0c \
    --role-arn arn:aws:iam::764531084004:role/LabRole \
    --profile voclabs/user2415006=Test_Student




./create-spot-instance.sh base gpi-model-z03g 120


./create-standard-instance.sh base gpi-model-z03gEC2_DIRECTION 15

    (Igual no me va a dejar por los custom limits ... )

        The following resource(s) failed to create: [Instance]. Rollback requested by user.
        2023-08-30 13:10:49 UTC-0300	Instance	
        
        CREATE_FAILED
        You have requested more vCPU capacity than your current vCPU limit of 0 allows for the instance bucket that the specified instance type belongs to. Please visit http://aws.amazon.com/contact-us/ec2-request to request an adjustment to this limit. (Service: AmazonEC2; Status Code: 400; Error Code: VcpuLimitExceeded; Request ID: 508ea01d-bacf-4c6c-95e9-1121f9a3b736; Proxy: null)



./create-standard-instance.sh base gpi-model-z03hEC2-WhatDir 15


        21:05



./create-standard-instance.sh base gpi-model-z03iEc2-xCCW 90









ubuntu@ip-172-31-34-103:~/deepracer-on-the-spot-pei$ ./create-standard-instance.sh base gpi-model-z03gEC2 120
+ baseResourcesStackName=base
+ shift
+ stackName=gpi-model-z03gEC2


        A las 17:50 Ingresando y por 120 minutos a las instnacias g de virginia...

        gpi-model-z03gEC2
                CREATE_COMPLETE	2023-08-30 17:50:05 UTC-0300	
                Setup a standard EC2 instance for deep racer



/create-standard-instance.sh base firstmodelbase 30 
./create-spot-instance.sh base firstmodelspot 30









*****************************************
*****************************************
*****************************************
*****************************************
*****************************************


***************************
Intra como codigo ...

    Dos ideas:

        a) Crear la SPOT pero no sobre la Spot ...

            ./create-spot-instance.sh base gpi-model-z03g 120



        b) Crear el pipeline en otra region ... (Africa)




*********************

warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams\EBWebView\GraphiteDawnCache\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams\EBWebView\ShaderCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams\EBWebView\ShaderCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams\EBWebView\ShaderCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams\EBWebView\ShaderCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams\EBWebView\ShaderCache\index. File/Directory is not readable.


download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/metrics/TrainingMetrics_2.json to ..\..\..\..\..\..\..\..\DOTS-model-z03f\metrics\TrainingMetrics_2.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/logs/deepracer-0_robomaker.4.semmin4z0ipgyriypcxkuwcnd.log to ..\..\..\..\..\..\..\..\DOTS-model-z03f\logs\deepracer-0_robomaker.4.semmin4z0ipgyriypcxkuwcnd.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/logs/tmpzvhrbujl_algo-1-lu0md_1.log to ..\..\..\..\..\..\..\..\DOTS-model-z03f\logs\tmpzvhrbujl_algo-1-lu0md_1.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/metrics/TrainingMetrics_3.json to ..\..\..\..\..\..\..\..\DOTS-model-z03f\metrics\TrainingMetrics_3.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/metrics/TrainingMetrics_4.json to ..\..\..\..\..\..\..\..\DOTS-model-z03f\metrics\TrainingMetrics_4.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/metrics/TrainingMetrics_5.json to ..\..\..\..\..\..\..\..\DOTS-model-z03f\metrics\TrainingMetrics_5.json
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\Settings\settings.dat. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\Settings\settings.dat.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\Settings\settings.dat.LOG2. File/Directory is not readable.
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/.coach_checkpoint to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\.coach_checkpoint
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/.ready 
to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\.ready

warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\SystemAppData\Helium\User.dat. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\SystemAppData\Helium\User.dat.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\SystemAppData\Helium\User.dat.LOG2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\SystemAppData\Helium\UserClasses.dat. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\SystemAppData\Helium\UserClasses.dat.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftTeams_8wekyb3d8bbwe\SystemAppData\Helium\UserClasses.dat.LOG2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AC\Temp\APPX.20w53c9h44bzwk63dhko5_ajb.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AC\Temp\APPX.aqbnpevfw_8dh3pmd5yjg0gtc.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AC\Temp\APPX.l6x6nutljn6o571exh76dydyb.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AC\Temp\APPX.mywltxu59vp_yvm6h6v3l1mwh.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AC\Temp\APPX.sr8zkwac2qbkzxccfxfzj7kpe.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AC\Temp\APPX.xup9gwddctfa066k2fhk4rgxh.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AppData\CacheStorage\CacheStorage.edb. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AppData\CacheStorage\CacheStorage.jfm. File/Directory is not readable.
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/103_Step-15910.ckpt.index to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\103_Step-15910.ckpt.index
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AppData\Indexed DB\edb.log. File/Directory is not readable.
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/106_Step-20095.ckpt.index to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\106_Step-20095.ckpt.index
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AppData\Indexed DB\edbtmp.log. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AppData\Indexed DB\IndexedDB.edb. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\AppData\Indexed DB\IndexedDB.jfm. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\Settings\settings.dat. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\Settings\settings.dat.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\Settings\settings.dat.LOG2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\lockfile. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\Cache\Cache_Data\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\Cache\Cache_Data\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\Cache\Cache_Data\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\Cache\Cache_Data\data_3. File/Directory is not readable.
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/103_Step-15910.ckpt.meta to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\103_Step-15910.ckpt.meta
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\Cache\Cache_Data\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\DawnCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\DawnCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\DawnCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\DawnCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\DawnCache\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\GPUCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\GPUCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\GPUCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\GPUCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\Default\GPUCache\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\GrShaderCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\GrShaderCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\GrShaderCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\GrShaderCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\GrShaderCache\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\GraphiteDawnCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\GraphiteDawnCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\GraphiteDawnCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\GraphiteDawnCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\GraphiteDawnCache\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\ShaderCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\ShaderCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\ShaderCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\ShaderCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\LocalState\EBWebView\ShaderCache\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\Settings\settings.dat. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\Settings\settings.dat.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\Settings\settings.dat.LOG2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\SystemAppData\Helium\User.dat. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\SystemAppData\Helium\User.dat.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\SystemAppData\Helium\User.dat.LOG2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\SystemAppData\Helium\UserClasses.dat. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\SystemAppData\Helium\UserClasses.dat.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\MicrosoftWindows.Client.WebExperience_cw5n1h2txyewy\SystemAppData\Helium\UserClasses.dat.LOG2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\PortraitDisplays.HPDisplayControl_2dgmkzkw4h30c\SystemAppData\Helium\User.dat. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\PortraitDisplays.HPDisplayControl_2dgmkzkw4h30c\SystemAppData\Helium\User.dat.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\PortraitDisplays.HPDisplayControl_2dgmkzkw4h30c\SystemAppData\Helium\User.dat.LOG2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\PortraitDisplays.HPDisplayControl_2dgmkzkw4h30c\SystemAppData\Helium\UserClasses.dat. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\PortraitDisplays.HPDisplayControl_2dgmkzkw4h30c\SystemAppData\Helium\UserClasses.dat.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Packages\PortraitDisplays.HPDisplayControl_2dgmkzkw4h30c\SystemAppData\Helium\UserClasses.dat.LOG2. File/Directory is not readable.
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/106_Step-20095.ckpt.meta to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\106_Step-20095.ckpt.meta
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03e/model/model_91.pb to ..\..\..\..\..\..\..\..\DOTS-model-z03e\model\model_91.pb
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/107_Step-21311.ckpt.index to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\107_Step-21311.ckpt.index
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/107_Step-21311.ckpt.meta to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\107_Step-21311.ckpt.meta
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/108_Step-22418.ckpt.index to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\108_Step-22418.ckpt.index
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\041d8a3e-bb04-4588-882d-21b613ecbb2f.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\0473a223-77b1-48d5-b81f-700e47d12422.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\0a96f7fc-763b-4322-b9fe-3b9029000cbb.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\0e3edfd9-c358-459a-a205-3447fb7738ed.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\0f9ce168-1436-4702-bc73-24fcadaa380e.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\1afd9815-70c6-4e66-bd2c-03502e31f181.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\1e5a9452-3a87-4606-9c30-fdd8bf6c04e1.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\1f06121f-6952-4065-b6a3-426d4cf68906.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\21044f49-68c1-4c01-85f1-3067d8a71b6f.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\21692420-9ed2-46cf-bf3e-f067201a4a37.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\220d2d85-2fb7-4a2e-b00b-4845e9f92a05.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\28e5114e-bb7b-4042-a98d-1a2dcc4fa200.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\2a6f8aef-dfd5-4da5-901a-a9de92fb0abd.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\316c46aa-b204-4ac9-b338-a75ea1c4e367.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\3afb515d-b575-4be8-a5a4-86d64d3fe9cf.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\46f34261-dd5e-4e3b-9f36-8896afdc7ffd.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\4b4b08f4-b4d7-43a9-99b5-26d3e51994cb.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\5846c96a-6e14-4b41-8844-7d71ba82b6c2.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\5b724884-6f90-4393-9cad-ca48dc83c7df.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\5d9a85c8-aae3-4738-9907-b766de4282d4.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\5f5cd8d3-7549-455c-a5ff-e180b08f9f48.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\63a5b958-a1ec-499a-871e-dd3fbf90771f.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\6a751f56-6ed8-46be-8fb6-3f83e1643522.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\6c5187a9-b9f4-495b-99ae-2b4ccbc8ec43.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\6d7894b1-cecd-45b2-b512-d40ac77622b6.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\72c7017a-b70d-47e3-a8f9-ea60768de7d8.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\7e587181-544f-459e-a7bd-fb97c1de835b.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\93818387-e9d0-425d-905e-d5774a9c2c75.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\94571965-7ffc-41f5-add7-002ec1481822.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\97e1bf1e-ace9-46e0-8f6f-fc6d8db8029d.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\9d01994d-2642-4180-a188-0d322a6b884e.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\9ff88c06-7355-43cd-b8c0-40978b75e195.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\a198ba69-0f85-42f4-b7cd-6bfc52da0b23.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\a5950e51-e90e-43e3-9078-a7eea2c3df51.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\aadb110a-a973-4042-a695-8929d6c9fa60.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\ad6417ad-f2a9-4a74-8cb6-648548512645.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\afd3a8e1-e714-4a10-94ac-6dcb18760ae7.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\be7acadf-1a32-4a07-8307-ba16019f4672.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\c1cf0b1e-aac8-4f7e-a126-b54425b7ccaf.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\c2835a34-0a49-4d7f-9616-f480777b65c5.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\c9c37482-c37e-4bd3-be0e-bfa70bae779c.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\cdaa8b68-4e0b-4471-bc42-7ea1657c18e5.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\d03622b3-9e88-43f0-8f96-a694520c4734.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\d5df22b1-a4c5-4a84-85ac-13e9be252d84.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\dad6fb52-e26c-4b2e-ade7-3d857958e3e9.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\e7d08ecf-3330-4cf7-977f-dbbc3493b91f.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\e90bdb5c-f82b-421b-b518-42b4cfa4b022.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\ea5fca93-3eb5-46c3-b772-59ad2381bd20.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\ec9df903-71ac-443d-a025-52e69a97cc07.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\f1a9a39c-0f84-46d2-9ba0-e40493de95c6.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\f69d4622-5d30-45d7-b285-90ad70a70d87.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\f9047d1d-1cfe-4222-a2f4-7e277dcf37c4.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\ff0668ea-adbe-415c-8e13-6fed949a266f.tmp. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Local\Temp\HFH84B2.tmp.dir. File/Directory is not readable.
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/108_Step-22418.ckpt.meta to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\108_Step-22418.ckpt.meta
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/deepracer_checkpoints.json to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\deepracer_checkpoints.json
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\Cache\Cache_Data\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\Cache\Cache_Data\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\Cache\Cache_Data\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\Cache\Cache_Data\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\Cache\Cache_Data\index. File/Directory is not readable.
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/103_Step-15910.ckpt.data-00000-of-00001 to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\103_Step-15910.ckpt.data-00000-of-00001
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\DawnCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\DawnCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\DawnCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\DawnCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\DawnCache\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\GPUCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\GPUCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\GPUCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\GPUCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Code\GPUCache\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\lockfile. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\Cache\Cache_Data\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\Cache\Cache_Data\data_1. File/Directory is not readable.   
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\Cache\Cache_Data\data_2. File/Directory is not readable.   
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\Cache\Cache_Data\data_3. File/Directory is not readable.   
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\Cache\Cache_Data\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\GPUCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\GPUCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\GPUCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\GPUCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Microsoft\Teams\GPUCache\index. File/Directory is not readable.
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/model_103.pb to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\model_103.pb
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/model_metadata.json to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\model_metadata.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/model_108.pb to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\model_108.pb
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/output.tar.gz to ..\..\..\..\..\..\..\..\DOTS-model-z03f\output.tar.gz
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/108_Step-22418.ckpt.data-00000-of-00001 to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\108_Step-22418.ckpt.data-00000-of-00001
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/reward_function.py to ..\..\..\..\..\..\..\..\DOTS-model-z03f\reward_function.py
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/107_Step-21311.ckpt.data-00000-of-00001 to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\107_Step-21311.ckpt.data-00000-of-00001
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/source/sourcedir.tar.gz to ..\..\..\..\..\..\..\..\DOTS-model-z03f\source\sourcedir.tar.gz
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/ip/done to ..\..\..\..\..\..\..\..\DOTS-model-z03g\ip\done
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0-viewer_proxy.1.rr0re4f1bl64ba8dpikfolihp.log to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\deepracer-0-viewer_proxy.1.rr0re4f1bl64ba8dpikfolihp.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/ip/ip.json to ..\..\..\..\..\..\..\..\DOTS-model-z03g\ip\ip.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/ip/hyperparameters.json to ..\..\..\..\..\..\..\..\DOTS-model-z03g\ip\hyperparameters.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/training_params.yaml to ..\..\..\..\..\..\..\..\DOTS-model-z03f\training_params.yaml
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_rl_coach.1.00gv0j3kqve93lvj9inp982br.log to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\deepracer-0_rl_coach.1.00gv0j3kqve93lvj9inp982br.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.1.r4369jrhwwgnzlplls1ubufgo.log to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\deepracer-0_robomaker.1.r4369jrhwwgnzlplls1ubufgo.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.2.zztxygiie7fryyb4ugvnw7lyu.log to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\deepracer-0_robomaker.2.zztxygiie7fryyb4ugvnw7lyu.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.4.tnrwu2ob22phis0ebz3g787gt.log to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\deepracer-0_robomaker.4.tnrwu2ob22phis0ebz3g787gt.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.5.owkn1v2r746zkvmhj9xs32al5.log to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\deepracer-0_robomaker.5.owkn1v2r746zkvmhj9xs32al5.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.6.5go07v86v4uapmd99echgs0es.log to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\deepracer-0_robomaker.6.5go07v86v4uapmd99echgs0es.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-analysis.log to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\deepracer-analysis.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/output.txt to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\output.txt
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/tmpwp469iiy_algo-1-qsg85_1.log to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\tmpwp469iiy_algo-1-qsg85_1.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/model.tar.gz to ..\..\..\..\..\..\..\..\DOTS-model-z03g\model.tar.gz
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/output.tar.gz to ..\..\..\..\..\..\..\..\DOTS-model-z03g\output.tar.gz
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/reward_function.py to ..\..\..\..\..\..\..\..\DOTS-model-z03g\reward_function.py
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/model/model_metadata.json to ..\..\..\..\..\..\..\..\DOTS-model-z03g\model\model_metadata.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/106_Step-20095.ckpt.data-00000-of-00001 to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\106_Step-20095.ckpt.data-00000-of-00001
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/source/sourcedir.tar.gz to ..\..\..\..\..\..\..\..\DOTS-model-z03g\source\sourcedir.tar.gz
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.3.xu6dxhpt6gap0xfdj1ymskiib.log to ..\..\..\..\..\..\..\..\DOTS-model-z03g\logs\deepracer-0_robomaker.3.xu6dxhpt6gap0xfdj1ymskiib.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/training_params.yaml to ..\..\..\..\..\..\..\..\DOTS-model-z03g\training_params.yaml
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model.tar.gz to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model.tar.gz
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/model_107.pb to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\model_107.pb
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03f/model/model_106.pb to ..\..\..\..\..\..\..\..\DOTS-model-z03f\model\model_106.pb
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\lockfile. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\Cache\Cache_Data\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\Cache\Cache_Data\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\Cache\Cache_Data\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\Cache\Cache_Data\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\Cache\Cache_Data\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\DawnCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\DawnCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\DawnCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\DawnCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\DawnCache\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\GPUCache\data_0. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\GPUCache\data_1. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\GPUCache\data_2. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\GPUCache\data_3. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\AppData\Roaming\Slack\GPUCache\index. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\Documents\My Music. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\Documents\My Pictures. File does not exist.
warning: Skipping file C:\\Users\pablo\Documents\My Videos. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\OneDrive - Fundación UADE\.849C9593-D756-4E56-8D6E-42412F2A707B. File/Directory is not readable.
warning: Skipping file C:\\Users\pablo\OneDrive - Fundación UADE\ACyT A21T03 - ML Sobre RRNN\A21T23 - Presentación Informe Final\Adjuntos Paso 03 - Papers Congresos\PAPER 03 - CACIC 2022 - AQUA III\28 CACIC 2022 - WASI - Predicción de incendios forestales mediante modelos de Machine Learning.pdf. File does not exist.
warning: Skipping file C:\\Users\pablo\OneDrive\.849C9593-D756-4E56-8D6E-42412F2A707B. File/Directory is not readable.
warning: Skipping file C:\\Windows\diagerr.xml. File/Directory is not readable.  
warning: Skipping file C:\\Windows\diagwrn.xml. File/Directory is not readable.
warning: Skipping file C:\\Windows\LiveKernelReports. File/Directory is not readable.
warning: Skipping file C:\\Windows\ModemLogs. File/Directory is not readable.
warning: Skipping file C:\\Windows\Prefetch. File/Directory is not readable.     
warning: Skipping file C:\\Windows\ServiceState. File/Directory is not readable. 
warning: Skipping file C:\\Windows\SystemTemp. File/Directory is not readable.   
warning: Skipping file C:\\Windows\Temp. File/Directory is not readable.
warning: Skipping file C:\\Windows\WUModels. File/Directory is not readable.     
warning: Skipping file C:\\Windows\Installer\MSIAD12.tmp. File/Directory is not readable.
warning: Skipping file C:\\Windows\Logs\SystemRestore. File/Directory is not readable.
warning: Skipping file C:\\Windows\PLA\Reports. File/Directory is not readable.  
warning: Skipping file C:\\Windows\PLA\Rules. File/Directory is not readable.
warning: Skipping file C:\\Windows\PLA\Templates. File/Directory is not readable.
warning: Skipping file C:\\Windows\PLA\System\System Diagnostics.xml. File/Directory is not readable.
warning: Skipping file C:\\Windows\PLA\System\System Performance.xml. File/Directory is not readable.
warning: Skipping file C:\\Windows\Panther\setupact.log. File/Directory is not readable.
warning: Skipping file C:\\Windows\Panther\setuperr.log. File/Directory is not readable.
warning: Skipping file C:\\Windows\Panther\UnattendGC\diagerr.xml. File/Directory is not readable.
warning: Skipping file C:\\Windows\Panther\UnattendGC\diagwrn.xml. File/Directory is not readable.
warning: Skipping file C:\\Windows\Panther\UnattendGC\setupact.log. File/Directory is not readable.
warning: Skipping file C:\\Windows\Panther\UnattendGC\setuperr.log. File/Directory is not readable.
warning: Skipping file C:\\Windows\Provisioning\Autopilot. File/Directory is not readable.
warning: Skipping file C:\\Windows\Resources\Themes\aero\VSCache. File/Directory is not readable.
warning: Skipping file C:\\Windows\ServiceProfiles\LocalService. File/Directory is not readable.
warning: Skipping file C:\\Windows\ServiceProfiles\NetworkService. File/Directory is not readable.
warning: Skipping file C:\\Windows\SysWOW64\config. File/Directory is not readable.
warning: Skipping file C:\\Windows\SysWOW64\Configuration. File/Directory is not readable.
warning: Skipping file C:\\Windows\SysWOW64\Msdtc. File/Directory is not readable.
warning: Skipping file C:\\Windows\SysWOW64\NetworkList. File/Directory is not readable.
warning: Skipping file C:\\Windows\SysWOW64\sru. File/Directory is not readable. 
warning: Skipping file C:\\Windows\SysWOW64\Tasks. File/Directory is not readable.
warning: Skipping file C:\\Windows\SysWOW64\Com\dmp. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\config. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\Configuration. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\DriverState. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\ias. File/Directory is not readable. 
warning: Skipping file C:\\Windows\System32\MsDtc. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\networklist. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\SleepStudy. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\sru. File/Directory is not readable. 
warning: Skipping file C:\\Windows\System32\Tasks. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\WDI. File/Directory is not readable. 
warning: Skipping file C:\\Windows\System32\WebThreatDefSvc. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\Com\dmp. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\LogFiles\WMI. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\Microsoft\Protect\Recovery\Recovery.dat. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\Microsoft\Protect\Recovery\Recovery.dat.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\Microsoft\Protect\Recovery\Recovery.dat.LOG2. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\Microsoft\Protect\Recovery\Recovery.dat{a312a340-0809-11ee-8400-005056c00008}.TM.blf. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\Microsoft\Protect\Recovery\Recovery.dat{a312a340-0809-11ee-8400-005056c00008}.TMContainer00000000000000000001.regtrans-ms. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\Microsoft\Protect\Recovery\Recovery.dat{a312a340-0809-11ee-8400-005056c00008}.TMContainer00000000000000000002.regtrans-ms. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\SMI\Store\Machine\SCHEMA.DAT. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\SMI\Store\Machine\SCHEMA.DAT.LOG1. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\SMI\Store\Machine\SCHEMA.DAT.LOG2. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\SMI\Store\Machine\SCHEMA.DAT{a2332f24-cdbf-11ec-8680-002248483d79}.TM.blf. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\SMI\Store\Machine\SCHEMA.DAT{a2332f24-cdbf-11ec-8680-002248483d79}.TMContainer00000000000000000001.regtrans-ms. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\SMI\Store\Machine\SCHEMA.DAT{a2332f24-cdbf-11ec-8680-002248483d79}.TMContainer00000000000000000002.regtrans-ms. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\Sysprep\Panther\diagerr.xml. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\Sysprep\Panther\diagwrn.xml. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\catroot2\edb.log. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\catroot2\edbtmp.log. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\catroot2\{127D0A1D-4EF2-11D1-8608-00C04FC295EE}\catdb. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\catroot2\{127D0A1D-4EF2-11D1-8608-00C04FC295EE}\catdb.jfm. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\catroot2\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}\catdb. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\catroot2\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}\catdb.jfm. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\drivers\DriverData. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\spool\PRINTERS. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\spool\SERVERS. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\MOF. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\00567E5D2A8D94901413112C325F9981.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\01A4AC44EF1F558F4C56A16AD4A5E4F6.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\02C1C442EB4740CBD57AFB5448BB0830.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\054DBF98A5BDEBA0516A14ECF5A20C2D.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\06C7FB7322D8613CB611574D175D5295.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\07C1BDDF9BC52067BD8EAA96B2B58467.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\082476FDCBDFB4F790A856288C54C164.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\0859AEAAD7351F9BFBDD25FE1DD07438.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\0A9DBC92D554324656F61F9862679F27.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\0C0DD8C1FFB363D1DF0C47032896A74F.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\0E4EBF3DFBF155BECC795836EEF54E10.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\151C37D1EE0423A33C47755F756F6A2E.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\152666125DF355B34B7474068D397F71.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\15483CFC61F37EAB14E86CBB49425396.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\18340690917B354A25F581DD5B52579A.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\19D20A61125316DF3493F46DDF4647FA.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\1A9A415FA4AFC55163F69A01E0468C0A.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\1DE7BE7BA35D977F49656C02C66058FC.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\20375C642DED520334DD8963CD139B20.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\20B127CD0E5F343CA0C6C6D1A27A31CB.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\21BD8E9B6A3575C7E6CFD05471F4DE86.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\21DF4C8F6241E13A9D59D014A691E8CF.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\23C6262469C234ABBEBF006A4864DB1F.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\24C894E7603576BAE4A5CD6F4223A5A4.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\26C097A9392F8C541AD42E89B7909073.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\26F20D3CF2EE890FA92A9EB21D91A591.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\27A6AB1D4CF2DB847D0E8870514E6B66.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\2A0B206CC9B7CD6E55D94F2E05C49D61.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\2AA23BB86A5EBD8BC2D820944E55B233.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\2AD569664F5ED1B2A81A2B93B5A493ED.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\2C6DF195444DC2947442EDBB95DF35D8.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\2CFDE82FD3064F09CBB2D4BEEF41F2B2.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\317A0811ADC41E940867412E307D0F88.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\317ABD51A1B3D5D4DA7817BF39D4A580.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\34A4B4A032D601C64A03F236C0092455.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\357EB0BDF149363AEE40135270773D7A.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\3640695FFB3AA9E29E9EBE7F703F9429.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\3893E327DC1BDFCE8350393770FCF510.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\389B9720F257CEBE3ABB0CFDCDA5A2D2.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\3A01647A9113490045B9D4AE10390941.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\409C534415BEB49E423AAD00667A77FF.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\42D4F767B244551D136575ED4E2AB6A2.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\4556FE20E34F685E332D41DEDA56952A.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\45997421E30BD4CC2633CF06A2914E6C.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\4A01E0F376B5833EBA98F0D1D5F60CD1.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\4CF4367D80BB224B93B823782C1CB69B.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\4D06958C26E8EE4ED93ADDC0E43A3DFB.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\50342F1DA2C6958FDD5A2462F1B25802.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\53361FCA5492832D2A8F49E617BE741A.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\53B6CF98F7C21632BA2F02B079EFF630.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\5415DB571936B839BA1570C49F144C90.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\567F4D257B3AD049F53285091D022261.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\56FDEC37E800897256718E58F3A50F6F.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\5966D45C7B25EACA46E87DD8E5703964.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\5A3D685CA4B50D7A6704B137800E6BC1.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\5FA987E018B4BD83065C1046F13808CF.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\61BB426110C2458F94DA0CEBF8A7C587.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\6393681F3FF86DF25BFA934035152391.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\63BE63AED68229DE1EE4E9D35358ED87.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\662D53B6400AF9DEE3040BC2A6D61DA7.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\6A3CBAC726AED9A9E2022984B282A28A.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\6B2E9B9DD48143300F311C13834506C2.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\6D525F7D9520481B01B4AA1E28BC8911.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\6EFAC6DC642FC970EFE930C34BA61A2D.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\7073EBB8E2F3C70E0FA1F650B7DEA970.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\74161B7FAE1A78C6FF7FF262B9EF72C6.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\758C343F1DE1B5150F2DCE7BF2305E41.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\7721EEBD217D47C862CC2E2575235843.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\78180A773E69999C917D0D1DFB1120D3.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\78FCA45D50EFEAA6AAD6DB14FFC9353B.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\7947D6F30D01272EFE76E6899B2E4BBF.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\797FAECDD6F439BC20998A3CDDBD9C55.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\7A76940A07CAC2ED30E215B850BE6101.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\7BA91B919FDEE5AC3B4D620C30064037.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\7D168EAC469673CDFDB33C16DADF4253.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\7E2203CA7615E40D788C4E848C53E697.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\81A8166E8EB115107E6D6297C46BBC66.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\81C82A52CC623BC64CA56E81005EFD39.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\8268BF28BB65399BF94A87987C442D38.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\85DF24201F61ADA3C95CE96A7411395E.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\8B5EFA10E7EFDE3ED3DC6490FAA2942A.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\8BA7B20A57ACB90C9251505BC53769A5.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\8C3ADEFE4C53DB30374C9848208BA4E0.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\90527F25FF8F20466B2A8C29C48A2859.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\912105CCEC67A49ACDE00816E0A721FA.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\95292B01814DAE6E1207A91A3ACE942F.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\96ECEEC481A353CD63047E54600304F8.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\9A5C244E07949EDF54B4C645670D4F2A.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\9A8A3F629EF64E8647E15C95F53D0355.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\9AB49D379159AF4E7483E61D8075C660.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\9AD3182A2F39A3E091E15109132EC6CC.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\9DDB9259CF8C44CD52C8D0932C75F96E.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\A014F3738A3456D61C86776C100FE08A.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\A0368C9C1F295D8AD6A3B19AD4D286B3.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\A48075DEFFEF447192179E52701BBB92.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\A515EDA43102D883701321DACCA85828.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\A58663026147D78763E0218852DB5798.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\A6877E1C1F41E6D58E3710A24708FC8C.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\AA789BFD65EA794D109B919CC5D0861D.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\ADC76C6473F1C3722A0A86C2A9AED340.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\ADE9A9750492C10B14DA28D4B92D198E.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\B06176DD23457B8CB2B128A87500CCEA.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\B15D0311BD29A1B7661EB8E56D93F20E.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\B1C0EC634DB6AFFE6A80B02D97D807C1.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\B213FBC8D5B7F097FB50E5FD3B90CF13.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\B2A29ED04BB7E80967FD2DE95AABC154.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\B3D1279CF76B72D4874D43A6EF458EF8.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\B70805B1D81CD151F4A6BABD680E325E.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\BA7C8C34F946F9001666E7AF75C1BA96.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\BF0A53505A9D675F8175CBA1EE97091F.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\C1EE3E23EA9AE55AFD38558BE35E3A52.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\C51C6B749222EB90D77FF002092046E3.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\C52B68177C4BDC82FED192C6B13782F6.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\C56957900550AEDB8827A99F7F88FF6B.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\C81C79212F23BFCD1E4AA8C008931EBA.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\CF51101DC59379E7F60810810207A111.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\CF9F89FB16D4A85FC0A6B023913149BF.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\D15D65345EE27D8E94D4637FAEA3A31E.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\D6260981A76E98693C2A64EFF833F1EA.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\D6EC828E5AFAC85D20D00820DA6E8156.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\D7033E5542C72385B38CC13650FADF94.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\D967E86BE9B087653EC5099C683DFCF8.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\D9B050B7A24E09624652E41AC4639DDE.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\DE8BDB1E98899331BA8BFCF137FA3C48.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\E04DE4CDFEC284A342159BB920976701.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\E67FE3B1B21C4E04D20694FAEBF701B1.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\E737DE61441445E1FDFCA45EF5E7D987.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\E7728CB5EC47D9287D3B4D5F4BFCB501.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\E797F65DBFCC69EEF33156C40942ACCD.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\E82E046A429396837946518D9CE5E409.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\F1E6F20419C0FB7E0955BDA831DF56B2.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\F3923002215DE6428F06AB1B9758ACC5.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\F5327279D02075EE4A56525C409CDD17.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\F62822D9285FD534B3B4C286D0711633.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\F7CDBAA892F4596D1C9D08892D786057.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\FB0CB3BBFF12037F8A84BE1A9146C9CB.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\FB197050E7085C76BA18924C630E458C.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\FC03EE25000B51516D0C7BC4562550DB.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\FC0FBEBEDA1F30CB076C805652C54DFA.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\wbem\AutoRecover\FE5D7E3DE1813E2423493BCDFF23AF93.mof. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Application.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\HardwareEvents.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\HP Analytics.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\HP Diagnostics.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Intel-GFX-Info%4Application.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Intel-GFX-Info%4System.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\IntelAudioServiceLog.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Internet Explorer.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Key Management Service.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Client-Licensing-Platform%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AAD%4Operational.evtx. File/Directory is not readable.  
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppID%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Application-Experience%4Program-Compatibility-Assistant.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Application-Experience%4Program-Compatibility-Troubleshooter.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Application-Experience%4Program-Inventory.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Application-Experience%4Program-Telemetry.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Application-Experience%4Steps-Recorder.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppLocker%4EXE and DLL.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppLocker%4MSI and Script.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppLocker%4Packaged app-Deployment.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppLocker%4Packaged app-Execution.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppModel-Runtime%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppReadiness%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppReadiness%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppXDeployment%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppXDeployment-Server%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppXDeploymentServer%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppXDeploymentServer%4Restricted.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-AppxPackaging%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Audio%4CaptureMonitor.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Audio%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Audio%4PlaybackManager.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Authentication User Interface%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-BackgroundTaskInfrastructure%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Biometrics%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-BitLocker%4BitLocker Management.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Bits-Client%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-CloudRestoreLauncher%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-CloudStore%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-CodeIntegrity%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Containers-BindFlt%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Containers-Wcifs%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Crypto-DPAPI%4BackUpKeySvc.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Crypto-DPAPI%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Crypto-NCrypt%4CertInUse.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Crypto-NCrypt%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider%4Autopilot.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-DeviceSetupManager%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-DeviceSetupManager%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Dhcp-Client%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Dhcpv6-Client%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Diagnosis-DPS%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Diagnosis-Scheduled%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Diagnosis-Scripted%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Diagnosis-Scripted%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Diagnostics-Performance%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-DiskDiagnosticDataCollector%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-EapHost%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-EapMethods-RasChap%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-EapMethods-RasTls%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-EnhancedStorage-EhStorClass%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Fault-Tolerant-Heap%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-FileHistory-Core%4WHC.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-GroupPolicy%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-HelloForBusiness%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Host-Network-Service-Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Host-Network-Service-Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-HotspotAuth%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Hyper-V-Hypervisor-Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Hyper-V-Hypervisor-Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Hyper-V-VmSwitch-Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-IKE%4Operational.evtx. File/Directory is not readable.  
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-Boot%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-Cache%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-Dump%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-EventTracing%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-LiveDump%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-PnP%4Configuration.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-PnP%4Device Management.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-PnP%4Driver Watchdog.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-Power%4Thermal-Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-ShimEngine%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-StoreMgr%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-WHEA%4Errors.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-WHEA%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Known Folders API Service.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-LanguagePackSetup%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-LAPS%4Operational.evtx. File/Directory is not readable. 
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-LiveId%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-ModernDeployment-Diagnostics-Provider%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-ModernDeployment-Diagnostics-Provider%4Autopilot.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-ModernDeployment-Diagnostics-Provider%4Diagnostics.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-ModernDeployment-Diagnostics-Provider%4ManagementService.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-MUI%4Admin.evtx. File/Directory is not readable.        
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-MUI%4Operational.evtx. File/Directory is not readable.  
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-NcdAutoSetup%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-NCSI%4Operational.evtx. File/Directory is not readable. 
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-NetworkProfile%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-NlaSvc%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Ntfs%4Operational.evtx. File/Directory is not readable. 
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Ntfs%4WHC.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Partition%4Diagnostic.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Perflib%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-PowerShell%4Admin.evtx. File/Directory is not readable. 
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-PowerShell%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-PrintService%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Privacy-Auditing%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Program-Compatibility-Assistant%4CompatAfterUpgrade.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Provisioning-Diagnostics-Provider%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Provisioning-Diagnostics-Provider%4AutoPilot.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Provisioning-Diagnostics-Provider%4ManagementService.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-PushNotification-Platform%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-PushNotification-Platform%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-ReadyBoost%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Regsvr32%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Resource-Exhaustion-Detector%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Resource-Exhaustion-Resolver%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-RestartManager%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Security-LessPrivilegedAppContainer%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Security-Mitigations%4KernelMode.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Security-Mitigations%4UserMode.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Security-SPP-UX-Notifications%4ActionCenter.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Shell-ConnectedAccountState%4ActionCenter.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Shell-Core%4ActionCenter.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Shell-Core%4AppDefaults.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Shell-Core%4LogonTasksChannel.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Shell-Core%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-ShellCommon-StartLayoutPopulation%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-SmbClient%4Audit.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-SmbClient%4Connectivity.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-SMBClient%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-SmbClient%4Security.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-SMBServer%4Audit.evtx. File/Directory is not readable.  
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-SMBServer%4Connectivity.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-SMBServer%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-SMBServer%4Security.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-StateRepository%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-StateRepository%4Restricted.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Storage-ClassPnP%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Storage-Storport%4Health.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Storage-Storport%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-StorageManagement%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-StorageSettings%4Diagnostic.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-StorageSpaces-Driver%4Diagnostic.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-StorageSpaces-Driver%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-StorageSpaces-ManagementAgent%4WHC.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Store%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Storsvc%4Diagnostic.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-TaskScheduler%4Maintenance.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-LocalSessionManager%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Time-Service%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-TWinUI%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-TZSync%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-UAC%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-UAC-FileVirtualization%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-UniversalTelemetryClient%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-User Device Registration%4Admin.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-User Profile Service%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-UserPnp%4ActionCenter.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-UserPnp%4DeviceInstall.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-UserSettingsBackup-BackupUnitProcessor%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-UserSettingsBackup-Orchestrator%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-VDRVROOT%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-VHDMP-Operational.evtx. File/Directory is not readable. 
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-VolumeSnapshot-Driver%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-VPN%4Operational.evtx. File/Directory is not readable.  
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Wcmsvc%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WebAuthN%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WER-Diag%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WER-PayloadHealth%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WerKernel%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WFP%4Operational.evtx. File/Directory is not readable.  
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Defender%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Defender%4WHC.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Firewall With Advanced Security%4ConnectionSecurity.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Firewall With Advanced Security%4FirewallDiagnostics.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WindowsBackup%4ActionCenter.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WindowsSystemAssessmentTool%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WindowsUpdateClient%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WinINet-Config%4ProxyConfigChanged.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Winlogon%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WinRM%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WLAN-AutoConfig%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WMI-Activity%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WorkFolders%4WHC.evtx. File/Directory is not readable.  
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WPD-ClassInstaller%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-Windows-WPD-MTPClassDriver%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Microsoft-WindowsPhone-Connectivity-WiFiConnSvc-Channel.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\OAlerts.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\OneApp_IGCC.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\PowerShellCore%4Operational.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Security.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Setup.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\System.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\System32\winevt\Logs\Windows PowerShell.evtx. File/Directory is not readable.
warning: Skipping file C:\\Windows\WinSxS\amd64_microsoft-windows-n..n_service_datastore_31bf3856ad364e35_10.0.22621.1992_none_b0e71267b1b72f7c\dnary.xsd. File/Directory is not readable.
warning: Skipping file C:\\Windows\WinSxS\amd64_microsoft-windows-n..n_service_datastore_31bf3856ad364e35_10.0.22621.674_none_3327464dff35e28c\dnary.xsd. File/Directory is not readable.
warning: Skipping file C:\\Windows\WinSxS\amd64_microsoft-windows-u..userpredictionmodel_31bf3856ad364e35_10.0.22621.1778_none_6ca449a093094efa\QualityUpdateMetadata.json. File/Directory is not readable.
warning: Skipping file C:\\Windows\WinSxS\amd64_microsoft-windows-u..userpredictionmodel_31bf3856ad364e35_10.0.22621.1778_none_6ca449a093094efa\Quwarning: Skipping filwarning: Skipping file C:\\Windows\WinSxS\amd64_microsoft-windows-u..userpredictionmodel_31bf3856ad364e35_10.0.22621.1778_none_6ca449a093094efa\QualityUpdateModel.txt. File/Directory is not readable.
warning: Skipping file C:\\Windows\WinSxS\amd64_microsoft-windows-u..userpredictionmodel_31bf3856ad364e35_10.0.22621.1778_none_6ca449a093094efa\QualityUpdateModelV2.onnx. File/Directory is not readable.
warning: Skipping file C:\\Windows\WinSxS\amd64_microsoft-windows-u..userpredictionmodel_31bf3856ad364e35_10.0.22621.1778_none_6ca449a093094efa\SBCModel.json. File/Directory is not readable.
warning: Skipping file C:\\Windows\WinSxS\amd64_microsoft-windows-u..userpredictionmodel_31bf3856ad364e35_10.0.22621.1778_none_6ca449a093094efa\SBCModel.txt. File/Directory is not readable.
fatal error:
PS>    .logsTmp/gpi_model_z03/
.logsTmp/gpi_model_z03/: The term '.logsTmp/gpi_model_z03/' is not recognized as a name of a cmdlet, function, script file, or executable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
PS C:\Users @ Data Disco D\code\deepracer-on-the-spot-pei\glaciar\012_PEI_Models\T2023-08\GPI_Series\gpi_model_z03>
PS C:\Users @ Data Disco D\code\deepracer-on-the-spot-pei\glaciar\012_PEI_Models\T2023-08\GPI_Series\gpi_model_z03> aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/ \aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/ \^C
PS C:\Users @ Data Disco D\code\deepracer-on-the-spot-pei\glaciar\012_PEI_Models\T2023-08\GPI_Series\gpi_model_z03> 




ubuntu@ip-172-31-34-103:~/deepracer-on-the-spot-pei/glaciar/012_PEI_Models/T2023-08/GPI_Series/gpi_model_z03$ aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/     .logsTmp/gpi_model_z03/
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/0/training-simtrace/15-iteration.csv to .logsTmp/gpi_model_z03/DOTS-model-z03g/0/training-simtrace/15-iteration.csv
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/1/training-simtrace/15-iteration.csv to .logsTmp/gpi_model_z03/DOTS-model-z03g/1/training-simtrace/15-iteration.csv
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/2/training-simtrace/15-iteration.csv to .logsTmp/gpi_model_z03/DOTS-model-z03g/2/training-simtrace/15-iteration.csv
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/3/training-simtrace/15-iteration.csv to .logsTmp/gpi_model_z03/DOTS-model-z03g/3/training-simtrace/15-iteration.csv
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/4/training-simtrace/15-iteration.csv to .logsTmp/gpi_model_z03/DOTS-model-z03g/4/training-simtrace/15-iteration.csv
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/output.txt to .logsTmp/gpi_model_z03/DOTS-model-z03g/logs/output.txt
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/5/training-simtrace/15-iteration.csv to .logsTmp/gpi_model_z03/DOTS-model-z03g/5/training-simtrace/15-iteration.csv
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics.json to .logsTmp/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics_1.json to .logsTmp/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics_1.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.3.w7ftqdfss9ij1ihmu3k6z35op.log to .logsTmp/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.3.w7ftqdfss9ij1ihmu3k6z35op.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics_2.json to .logsTmp/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics_2.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.4.9p947ddmxlfi2bsx287smvhqz.log to .logsTmp/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.4.9p947ddmxlfi2bsx287smvhqz.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.1.mcjdlavurr8lzgrhkqsfgzppe.log to .logsTmp/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.1.mcjdlavurr8lzgrhkqsfgzppe.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics_5.json to .logsTmp/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics_5.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics_3.json to .logsTmp/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics_3.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics_4.json to .logsTmp/gpi_model_z03/DOTS-model-z03g/metrics/TrainingMetrics_4.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/tmp1e9g0uz3_algo-1-pyq2t_1.log to .logsTmp/gpi_model_z03/DOTS-model-z03g/logs/tmp1e9g0uz3_algo-1-pyq2t_1.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.2.sxsje0vu5w9xx1suf0ipe6ni5.log to .logsTmp/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.2.sxsje0vu5w9xx1suf0ipe6ni5.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.6.ud74zjnkn8hf5x6jom0zox2d4.log to .logsTmp/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.6.ud74zjnkn8hf5x6jom0zox2d4.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.5.2xxc76gwmarrndwsm666yd91k.log to .logsTmp/gpi_model_z03/DOTS-model-z03g/logs/deepracer-0_robomaker.5.2xxc76gwmarrndwsm666yd91k.log
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/model/124_Step-26070.ckpt.index to .logsTmp/gpi_model_z03/DOTS-model-z03g/model/124_Step-26070.ckpt.index
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/model/124_Step-26070.ckpt.meta to .logsTmp/gpi_model_z03/DOTS-model-z03g/model/124_Step-26070.ckpt.meta
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/model/deepracer_checkpoints.json to .logsTmp/gpi_model_z03/DOTS-model-z03g/model/deepracer_checkpoints.json
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/output.tar.gz to .logsTmp/gpi_model_z03/DOTS-model-z03g/output.tar.gz
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/model.tar.gz to .logsTmp/gpi_model_z03/DOTS-model-z03g/model.tar.gz
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/model/124_Step-26070.ckpt.data-00000-of-00001 to .logsTmp/gpi_model_z03/DOTS-model-z03g/model/124_Step-26070.ckpt.data-00000-of-00001
download: s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/DOTS-model-z03g/model/model_124.pb to .logsTmp/gpi_model_z03/DOTS-model-z03g/model/model_124.pb
ubuntu@ip-172-31-34-103:~/deepracer-on-the-spot-pei/glaciar/012_PEI_Models/T2023-08/GPI_Series/gpi_model_z03$
