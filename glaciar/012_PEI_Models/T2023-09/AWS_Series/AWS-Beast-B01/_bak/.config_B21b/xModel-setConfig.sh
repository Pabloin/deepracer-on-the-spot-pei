#!/usr/bin/env bash

ls -la   ~/deepracer-on-the-spot-pei/custom-files
rm -r    ~/deepracer-on-the-spot-pei/custom-files

mkdir -p ~/deepracer-on-the-spot-pei/custom-files

## De esta config
cp   ./run.env                 ~/deepracer-on-the-spot-pei/custom-files
cp   ./reward_function.py      ~/deepracer-on-the-spot-pei/custom-files
cp   ./model_metadata.json     ~/deepracer-on-the-spot-pei/custom-files
cp   ./hyperparameters.json   ~/deepracer-on-the-spot-pei/custom-files

## De la Base
cp   ../system.env             ~/deepracer-on-the-spot-pei/custom-files


ls   -la   ~/deepracer-on-the-spot-pei/custom-files

echo "\n ---- [ run.env ] ---"
head -35   ~/deepracer-on-the-spot-pei/custom-files/run.env 

echo "\n ---- [ system.env ] ---"
head -15   ~/deepracer-on-the-spot-pei/custom-files/system.env   



# LAS SERIES
# WOLF: https://youtu.be/11Sta3idwZI?si=xcqUWXzMJ1W_WOcB&t=212
#