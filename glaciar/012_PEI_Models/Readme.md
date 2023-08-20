Experimentos de mis modelos

VERSION 
- PEI
- Student

---------------------
Fecha
2023-06-28


---------------------
Infra
Spot 5c.2xl


Carls Lars Track 

----------------

Resources

https://www.youtube.com/watch?v=eHRi0QfumUo

Matías
https://dev.to/mkreder/train-deepracer-models-on-ec2-spot-instances-4ndm

Original:
https://aws-deepracer-community.github.io/deepracer-for-cloud/

   Pasos:

         https://github.com/Pabloin/deepracer-for-cloud-pei.git 

         git config user.name Pabloin
         git config user.email pablo.ezequiel.inchausti@gmail.com


         cd deepracer-for-cloud-pei && ./bin/prepare.sh

         .....
         First stage done. Please reboot and run init.sh -c aws -a cpu

*** System restart required ***

         ./bin/init.sh -c aws -a cpu                 # aCloudGuru Server  ./bin/init.sh -c local -a cpu
         source bin/activate.sh

         -- Actualizar ~/ 
         cp ~/deepracer-for-cloud-pei/system.env.pei ~/deepracer-for-cloud-pei/system.env
         dr-update

# Entrenar:
         dr-upload-custom-files

       # dr-stop-training
         dr-start-training


........................................
Para el Viewer

      dr-update-viewer


      . BTW, always remember to dr-stop-training before dr-start-training.
      
        https://github.com/aws-deepracer-community/deepracer-for-cloud/issues/73


----------------


aws s3 mv s3://deep-racer-logs-glaciar/rl-deepracer-sagemaker s3://deep-racer-logs-glaciar/rl-deepracer-sagemaker_v01 --recursive





********************

Install Docker
      basado en:
      https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04

      sudo usermod -aG sudo cloud_user
      
      sudo apt update
      sudo apt dist-upgrade -y
      sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
      echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
      sudo apt update
      apt-cache policy docker-ce
      sudo systemctl status docker
      sudo usermod -aG docker ${USER}
      docker



      ---
      sudo su

                  /bin/prepare.sh -c local -a cpu
                  sudo shutdown -r now


                  ./bin/init.sh -c local -a cpu
                  source bin/activate.sh




---------------------
Experiments:

      dSeries = Default Derivats

            d01 - Default
            d02 - Default con cinco puntos
            
      wSeries = Waypints Derivates
      
            w01 - Waypoints

------------------

Envs

      deepracer-for-cloud
      DR_WORLD_NAME
      Carls Lars Track 
      DR_WORLD_NAME=reInvent2019_track

                  thunder_hill_pro_cw.npy
                  thunder_hill_pro.npy
                  thunder_hill_pro_ccw.npy

                  2022_march_pro_ccw.npy 
                  2022_march_pro.npy 
                  2022_march_pro_cw.npy

----------------

      run.env
      DR_WORLD_NAME : Track name on which you want to train your model on (not the one you see on console). 
      Refer the track name from this github repo. Example : 
            To train on Rogue Raceway, use 2022_march_pro   as the world name.
            To train on Lars Circuit,  use thunder_hill_pro as the world name.


--------------

      https://medium.com/@calmarianet/3-formas-de-ejecutar-comandos-en-segundo-plano-en-linux-9dedb779ca7d

      nohup ./my-shell-script.sh &
      nohup ./my-shell-script.sh > foo.out 2> foo.err < /dev/null &

      screen ./my-shell-script.sh
      screen -ls
      screen -r 1788.ttys000.milleniumfalcon