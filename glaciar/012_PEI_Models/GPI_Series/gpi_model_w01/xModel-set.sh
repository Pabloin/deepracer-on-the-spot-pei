#!/usr/bin/env bash

export MODEL_NAME=gpi_model_w01
export MODEL_PATH=~/deepracer-on-the-spot-pei/glaciar/012_PEI_Models/GPI_Series/$MODEL_NAME

cp ${MODEL_PATH}/hyperparameters.json   ~/deepracer-on-the-spot-pei/custom_files
cp ${MODEL_PATH}/model_metadata.json    ~/deepracer-on-the-spot-pei/custom_files
cp ${MODEL_PATH}/reward_function.py     ~/deepracer-on-the-spot-pei/custom_files

cp ${MODEL_PATH}/config/run.env.pei     ~/deepracer-on-the-spot-pei/run.env
cp ${MODEL_PATH}/config/system.env.pei  ~/deepracer-on-the-spot-pei/system.env