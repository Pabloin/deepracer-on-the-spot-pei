Model The Africa Beast ... 


       ./create-spot-instance-africa.sh     base-africa aws-africa-A01      120  
       ./create-standard-instance.sh base-africa aws-africa-A01      120

------------------------------------------------
AFRICA-A01:
       ./create-spot-instance-africa.sh         base-africa          aws-africa-A01a    120    (WIP)
              Este no paso al stack ... se quedo esperando ... 

       ./create-standard-instance-africa.sh     base-africa-s3pei    aws-africa-A02a    120    (WIP)
              Este completo el stack CFN pero despues no generaba logs ni modelos ni nada ... 
AFRICA-A02:


       Podria probar cruzado:

              ./create-standard-instance-africa.sh       base-africa          aws-africa-A01aTest    30




********************
Update 23/09/2023

       - El problema que tengo con Africa es que, no se porqué... me dejaron de funcionar los pipelines...
       - Capaz era por el error de la region dentro del YAML que no permitira escribir o acceder a s3 pero eso creo que ya lo solucione...

              - Entocnes debería lanzaro con el tiempo suficiente para hacer debug ...
              - O sea... 
                     Capaz una o dos horas (total después cancelo a CF)
                     y debería acceder a la instancia spot para ver los dockers ... 
                     eso creo que sería ..
                            - aunque primero revisar a que es lo que estoy lanzando ... 
                            - Duda ...
                                   ¿En el proyecto... Logré tener una instancia de africa funcionando... ?
                                   ¿Cuando se rompio?
                                   Cre que cuando detuve al pipeline.... 
                                   Igual, a la última imagen disponible la tengo ...       


a) Ejecutamos:



       ./create-standard-instance-africa.sh       base-africa          aws-africa-A01aDoa    60



********************


------------------------------------------------

Africa (Cape Town) af-south-1	

       base-africa        --s3:    base-africa-bucket-eqt69ynz6hf4	
       base-africa-s3pei  --s3:    base-africa-bucket-pei





       idea .. Entrenar cada pista ... 


---------------------
Ultima instancia OK en Africa:

.0.2/13 	AMI	Sep 11, 2023 9:00 PM	Available	
-
arn:aws:imagebuilder:af-south-1:845305768689:image/ubuntuserverfordeepracer-base-africa-ami/0.0.2/13	

/aws/imagebuilder/UbuntuServerForDeepRacer-base-africa-ami/0.0.2/13 

