Model pei

-----------------------
Z01 con Waypoints


 ./create-spot-instance.sh base gpi-model-z01 60


-----------------------
Enviados 

    - z02 Expectativa: IDEM z01 y z02
     pero con reward de velocidad  
        
    - Traer también a la funcion...
        Que continue del entrenamiento anterior ... 


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
                                                  .logsTmp/gpi_model_z03/FASE-01

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

aws s3 cp .logsTmp/  \ 
    s3://dr-models-glaciar-dots/  \ 
    --recursive  \ 
    --profile voclabs/user1587290=PABLO_EZEQUIEL_INCHAUSTI 


aws s3 sync .logsTmp/gpi_model_z03/  \ 
    s3://dr-models-glaciar-dots/gpi_model_z03/  \ 
    --profile voclabs/user1587290=PABLO_EZEQUIEL_INCHAUSTI 



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
    --name F01-DOTS-model-z03a  \
    --model-artifacts-s3-path s3://dr-models-glaciar-dots/gpi_model_z03/FASE-01/DOTS-model-z03a \
    --role-arn arn:aws:iam::983552762508:role/LabRole  \
    --profile voclabs/user1587290=PABLO_EZEQUIEL_INCHAUSTI


        Inicia Ealuacion: (la consola)  (Aca tengo que evaluar nada mas... no tengo que entrenar...)

            23:42 min ...   


            c) Medir:

                    - Darle otra vuelta de entrenamiento (de 5 horas?)
                    - Ojo con el Nohup ... 

                        -  Igual ... creo que Nohup no hay problema en DOTS porque el que entrena 
                                     es el Terraform ... 





***************************************************************************************************


***************************************************************************************************
Entrenamiento 1:

    Inicia - 27 Aug 2023 21:31:35
             ./create-spot-instance.sh base gpi-model-z03a 60 
              (Seccion Anterior)

Entrenamiento 2:
    Inicia - 27 Aug 2023 23:44:35
             ./create-spot-instance.sh base gpi-model-z03a 180

                OJO! 
                Agergaue                 
                #DR_LOCAL_S3_PRETRAINED=False
                DR_LOCAL_S3_PRETRAINED=True
                
             3 horas ...  

             ... SPOT Creado OK! (En virginia)

