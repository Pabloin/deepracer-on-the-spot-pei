#!/usr/bin/env bash

export MODEL_NAME=gpi_model_z01
export MODEL_PATH=~/deepracer-on-the-spot-pei/glaciar/012_PEI_Models/T2023-08/GPI_Series/$MODEL_NAME


rm ~/deepracer-on-the-spot-pei/custom-files/*.json 
rm ~/deepracer-on-the-spot-pei/custom-files/README.md 
rm ~/deepracer-on-the-spot-pei/custom-files/reward_function.py 
rm ~/deepracer-on-the-spot-pei/custom-files/run.env 
rm ~/deepracer-on-the-spot-pei/custom-files/system.env


cp ${MODEL_PATH}/hyperparameters.json   ~/deepracer-on-the-spot-pei/custom-files
cp ${MODEL_PATH}/model_metadata.json    ~/deepracer-on-the-spot-pei/custom-files
cp ${MODEL_PATH}/reward_function.py     ~/deepracer-on-the-spot-pei/custom-files

cp ${MODEL_PATH}/run.env                ~/deepracer-on-the-spot-pei/custom-files
cp ${MODEL_PATH}/system.env             ~/deepracer-on-the-spot-pei/custom-files

