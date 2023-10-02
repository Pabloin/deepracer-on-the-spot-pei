#!/usr/bin/env bash

ls -la   ~/deepracer-on-the-spot-pei/custom-files
rm -r    ~/deepracer-on-the-spot-pei/custom-files

mkdir -p ~/deepracer-on-the-spot-pei/custom-files

## De esta config
cp   ./run.env                 ~/deepracer-on-the-spot-pei/custom-files/run.env
cp   ./reward_function.py      ~/deepracer-on-the-spot-pei/custom-files
cp   ./model_metadata.json     ~/deepracer-on-the-spot-pei/custom-files

## De la Base
cp   ../hyperparameters.json   ~/deepracer-on-the-spot-pei/custom-files
cp   ../system.env             ~/deepracer-on-the-spot-pei/custom-files


ls   -la   ~/deepracer-on-the-spot-pei/custom-files

echo "\n ---- [ run.env ] ---"
head -25   ~/deepracer-on-the-spot-pei/custom-files/run.env 

echo "\n ---- [ system.env ] ---"
head -15   ~/deepracer-on-the-spot-pei/custom-files/system.env   
