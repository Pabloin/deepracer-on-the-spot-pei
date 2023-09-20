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

