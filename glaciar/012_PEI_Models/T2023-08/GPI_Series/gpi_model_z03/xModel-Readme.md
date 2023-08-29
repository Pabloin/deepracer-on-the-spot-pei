Model pei

-----------------------
Z01 con Waypoints


 ./create-spot-instance.sh base gpi-model-z01 60



------------------------
[AGOTADO]
    ALLv1-21047-Educator
    AWS Academy Learner Lab - Educator

[WIP]
    voclabs/user2410571=Test_Student
    AWS Academy Learner Lab [32691]
    Used $89.7 of $100


-----------------------
Enviados 

    - z02 Expectativa: IDEM z01 y z02
        pero con reward de velocidad                (OK)  
        
    - Traer también a la funcion...
        Que continue del entrenamiento anterior ... (OK)


        ¿Puedo hacer algo por laps? 
        Saber en que lap estoy ...

        run.env
        DR_LOCAL_S3_PRETRAINED=True

        DeepRacer On The Spot - Increment Training
        https://www.youtube.com/watch?v=9y5wx7fQUgc&list=PL9qmHoKq77dTFS59WjHciNb0a0n0dE8iF



    Duda:
        ¿Como si si entreno 
            Track direction
            Select the direction in which you wish to race.
            Clockwise
            Counterclockwise

            ... los debería tener en en los logs de Fase 1
_____________________________
TODO:

    - Los hiperparametros discretos también 
      fueron calculados por la tesis ... 
_____________________________

**********************************
Logs

    base-bucket-1f3pfk38sjoqu
    gpi_model_z03/
    s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/


    aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/ .logsTmp/gpi_model_z03

***************************************************************************************************
Entrenamiento 1:

    Inicia - 27 Aug 2023 21:31:35
             ./create-spot-instance.sh base gpi-model-z03a 60 

             SPOT Creado OK! (En virginia)


    Finaliza - 27 Aug 2023 21:31:35
            
             Deleting in Progress...
    Luego:

            a) Bajar los Logs de la Fase I

                aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/ \ 
                                                  .logsTmp/gpi_model_z03/

                Ok

            b) Bajar Modelo y evaluar en Academy de PEI (lo hago fruta dentro de poco ... )

                Upload S3 Academy

                export AWS_EDU_PROFILE_STD=voclabs/user2481293=Test_Student
                export AWS_EDU_PROFILE_PEI=voclabs/user1587290=PABLO_EZEQUIEL_INCHAUSTI
                export AWS_EDU_PROFILE=TBD

                export AWS_EDU_LABROLE_STD=arn:aws:iam::305834167779:role/LabRole
                export AWS_EDU_LABROLE_PEI=arn:aws:iam::983552762508:role/LabRole
                export AWS_EDU_LABROLE=TBD


voclabs/user1587290=PABLO_EZEQUIEL_INCHAUSTI

aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/ \
    .logsTmp/gpi_model_z03/  

aws s3 sync .logsTmp/gpi_model_z03/  \
    s3://dr-models-glaciar-dots/gpi_model_z03/  \
    --profile voclabs/user1587290=PABLO_EZEQUIEL_INCHAUSTI 

---------------------------------------
[WIP]
    voclabs/user2410571=Test_Student
    AWS Academy Learner Lab [32691]
    Used $89.7 of $100


aws s3 sync .logsTmp/gpi_model_z03/  \
    s3://dr-models-glaciar-dots-std571/gpi_model_z03/  \
    --profile voclabs/user2410571=Test_Student



echo "Siguiente Comando (Copy Paste):"
echo ""
echo " aws deepracer import-model   \ "
echo "         --type REINFORCEMENT_LEARNING   \ "
echo "         --name ${MODEL_VERSION}         \ "
echo "         --model-artifacts-s3-path s3://${S3_REPO_TARGET}/${MODEL}/${MODEL_VERSION} \   "
echo "         --role-arn ${AWS_EDU_LABROLE}   \ "
echo "         --profile  ${AWS_EDU_PROFILE}     "
echo ""




# Ejemplo OK

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z03a  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots/gpi_model_z03/DOTS-model-z03a \
    --role-arn arn:aws:iam::983552762508:role/LabRole  \
    --profile voclabs/user1587290=PABLO_EZEQUIEL_INCHAUSTI


 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z03b  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots/gpi_model_z03/DOTS-model-z03b \
    --role-arn arn:aws:iam::983552762508:role/LabRole  \
    --profile voclabs/user1587290=PABLO_EZEQUIEL_INCHAUSTI

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z03c  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots/gpi_model_z03/DOTS-model-z03c \
    --role-arn arn:aws:iam::983552762508:role/LabRole  \
    --profile voclabs/user1587290=PABLO_EZEQUIEL_INCHAUSTI


 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z03cBis2  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots/gpi_model_z03/DOTS-model-z03c \
    --role-arn arn:aws:iam::983552762508:role/LabRole  \
    --profile voclabs/user1587290=PABLO_EZEQUIEL_INCHAUSTI




        Inicia Ealuacion: (la consola)  (Aca tengo que evaluar nada mas... no tengo que entrenar...)

            23:42 min ...   
            23:52 min ...     (las tres laps)
            23:52 min ...     (las tres laps)
            

            c) Medir:

                    - Darle otra vuelta de entrenamiento (de 5 horas?)
                    - Ojo con el Nohup ... 

                        -  Igual ... creo que Nohup no hay problema en DOTS porque el que entrena 
                                     es el Terraform ... 



            Trial
            Time (MM:SS.mmm)
            Trial results (% track completed)
            Status
            Off-track
            Off-track penalty
            Crashes
            Crash penalty
            1	01:11.654	100%	Lap complete	10	20 seconds	0	--
            2	01:06.061	100%	Lap complete	8	16 seconds	0	--
            3	01:09.995	100%	Lap complete	10	20 seconds	0	--


***************************************************************************************************


***************************************************************************************************
Entrenamiento 1:

    Inicia - 27 Aug 2023 21:31:35
             ./create-spot-instance.sh base gpi-model-z03a 60 
              (Seccion Anterior)

Entrenamiento 2:
    Inicia - 28 Aug 2023 00:36:35
             ./create-spot-instance.sh base gpi-model-z03b 180

             ./create-spot-instance.sh base gpi-model-z03c 240



    Finalizara... - 28 Aug 2023 03:36:35

                OJO! 
                Agergaue                 
                #DR_LOCAL_S3_PRETRAINED=False
                DR_LOCAL_S3_PRETRAINED=True

                Siguiendo a:
                https://finlaymacrae.medium.com/easy-start-guide-for-deepracer-on-cloud-in-aws-4206db2ac6d0

                DR_LOCAL_S3_MODEL_PREFIX=gpi_model_z03/DOTS-model-z03b
                DR_LOCAL_S3_PRETRAINED=True
                DR_LOCAL_S3_PRETRAINED_PREFIX=gpi_model_z03/DOTS-model-z03a

                    1. If the instance is terminated, re-pull the instance and continue the last training
                    Please do the following #### ①. Modify the run.env file and modify the following parameters

                    DR_LOCAL_S3_MODEL_PREFIX=<The directory where the S3 bucket is stored for this training>
                    DR_LOCAL_S3_PRETRAINED=True
                    DR_LOCAL_S3_PRETRAINED_PREFIX=<The directory where the last training S3 bucket is stored>
                    DR_LOCAL_S3_PRETRAINED_CHECKPOINT=best

                https://segmentfault.com/a/1190000041988531/en

                (Esto implica ... que no necesito las fases (1,2,3 etc ... ))


             3 horas ...  

             ... SPOT  .... en virginia....

             ... la preocupacion es que me lo den.. 


***************************************************************************************************
Entrenamiento 1:

    Inicia - 27 Aug 2023 21:31:35
             ./create-spot-instance.sh base gpi-model-z03a 60 
              (Seccion Anterior)

Entrenamiento 2:
    Inicia - 28 Aug 2023 00:36:35
             ./create-spot-instance.sh base gpi-model-z03b 180

                    DOTS-model-z03b

                    Trial
                    Time (MM:SS.mmm)
                    Trial results (% track completed)
                    Status
                    Off-track
                    Off-track penalty
                    Crashes
                    Crash penalty
                    1	01:17.733	100%	Lap complete	15	30 seconds	0	--
                    2	01:26.811	100%	Lap complete	18	36 seconds	0	--
                    3	01:10.662	100%	Lap complete	14	28 seconds	0	--



Entrenamiento 3:
    Inicia - 28 Aug 2023 11:47:00
             ./create-spot-instance.sh base gpi-model-z03c 120

                    DOTS-model-z03cBis

                    Trial
                    Time (MM:SS.mmm)
                    Trial results (% track completed)
                    Status
                    Off-track
                    Off-track penalty
                    Crashes
                    Crash penalty
                    1	01:11.526	100%	Lap complete	11	22 seconds	0	--
                    2	01:11.412	100%	Lap complete	11	22 seconds	0	--
                    3	01:17.877	100%	Lap complete	14	28 seconds	0	--


                    DOTS-model-z03cBis2
                    Trial
                    Time (MM:SS.mmm)
                    Trial results (% track completed)
                    Status
                    Off-track
                    Off-track penalty
                    Crashes
                    Crash penalty
                    1	01:19.633	100%	Lap complete	14	28 seconds	0	--
                    2	01:19.193	100%	Lap complete	14	28 seconds	0	--
                    3	01:08.137	100%	Lap complete	10	20 seconds	0	--

                    DOTS-model-z03c1
                    Trial
                    Time (MM:SS.mmm)
                    Trial results (% track completed)
                    Status
                    Off-track
                    Off-track penalty
                    Crashes
                    Crash penalty
                    1	01:08.008	100%	Lap complete	10	20 seconds	0	--
                    2	01:19.727	100%	Lap complete	14	28 seconds	0	--
                    3	01:21.073	100%	Lap complete	15	30 seconds	0	--


Entrenamiento 4:
    ./create-spot-instance.sh base gpi-model-z03d 180
    }    Inicia - 28 Aug 2023 14:08:00



    ./create-spot-instance.sh base gpi-model-z03d 180
        Inicia: Mon Aug 28 19:30:54 
        Fin 22:48


                    Trial
                    Time (MM:SS.mmm)
                    Trial results (% track completed)
                    Status
                    Off-track
                    Off-track penalty
                    Crashes
                    Crash penalty
                    1	01:03.877	100%	Lap complete	7	14 seconds	0	--
                    2	00:58.932	100%	Lap complete	5	10 seconds	0	--
                    3	01:01.323	100%	Lap complete	6	12 seconds	0	--


                    Buenisimo!!!


                    Trial
                    Time (MM:SS.mmm)
                    Trial results (% track completed)
                    Status
                    Off-track
                    Off-track penalty
                    Crashes
                    Crash penalty
                    1	00:57.808	100%	Lap complete	5	10 seconds	0	--
                    2	00:56.844	100%	Lap complete	5	10 seconds	0	--
                    3	00:59.523	100%	Lap complete	5	10 seconds	0	--


                    ... Mejor ... (y está en wip)


    ./create-spot-instance.sh base gpi-model-z03e 120

            ubuntu@ip-172-31-34-103:~/deepracer-on-the-spot-pei$ ./create-spot-instance.sh base gpi-model-z03e 120
            Tue Aug 29 01:50:13 UTC 2023



---------------------------------------
[WIP]
    voclabs/user2410571=Test_Student
    AWS Academy Learner Lab [32691]
    Used $89.7 of $100
    arn:aws:iam::001726842821:role/LabRole

aws s3 sync s3://base-bucket-1f3pfk38sjoqu/gpi_model_z03/ \
    .logsTmp/gpi_model_z03/  
    
aws s3 sync .logsTmp/gpi_model_z03/  \
    s3://dr-models-glaciar-dots-std571/gpi_model_z03/  \
    --profile voclabs/user2410571=Test_Student

 aws deepracer import-model \
    --type REINFORCEMENT_LEARNING \
    --name DOTS-model-z03eWIP2  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots-std571/gpi_model_z03/DOTS-model-z03e \
    --role-arn arn:aws:iam::001726842821:role/LabRole \
    --profile voclabs/user2410571=Test_Student
