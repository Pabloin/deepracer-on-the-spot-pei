#!/usr/bin/env bash

export MODEL_NAME=gpi_model_w01
export MODEL_PATH=~/deepracer-on-the-spot-pei/glaciar/012_PEI_Models/T2023-08/GPI_Series/$MODEL_NAME


ls -la   ~/deepracer-on-the-spot-pei/custom-files
mkdir -p ~/deepracer-on-the-spot-pei/custom-files

cp ${MODEL_PATH}/hyperparameters.json   ~/deepracer-on-the-spot-pei/custom-files
cp ${MODEL_PATH}/model_metadata.json    ~/deepracer-on-the-spot-pei/custom-files
cp ${MODEL_PATH}/reward_function.py     ~/deepracer-on-the-spot-pei/custom-files

cp ${MODEL_PATH}/run.env                ~/deepracer-on-the-spot-pei/custom-files
cp ${MODEL_PATH}/system.env             ~/deepracer-on-the-spot-pei/custom-files

ls   -la   ~/deepracer-on-the-spot-pei/custom-files
head -40   ~/deepracer-on-the-spot-pei/custom-files/run.env



