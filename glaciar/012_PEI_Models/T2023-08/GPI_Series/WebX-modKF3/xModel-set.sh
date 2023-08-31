#!/usr/bin/env bash

ls -la   ~/deepracer-on-the-spot-pei/custom-files
mkdir -p ~/deepracer-on-the-spot-pei/custom-files

cp   ./hyperparameters.json   ~/deepracer-on-the-spot-pei/custom-files
cp   ./model_metadata.json    ~/deepracer-on-the-spot-pei/custom-files
cp   ./reward_function.py     ~/deepracer-on-the-spot-pei/custom-files

cp   ./run.env                ~/deepracer-on-the-spot-pei/custom-files
cp   ./system.env             ~/deepracer-on-the-spot-pei/custom-files


ls   -la   ~/deepracer-on-the-spot-pei/custom-files
head -40   ~/deepracer-on-the-spot-pei/custom-files/run.env  


