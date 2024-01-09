#!/bin/zsh

sleep 20

open -a "OBS"

sleep 10

cd ~/Desktop/obs-control
pwd
source venv/bin/activate 
python main.py

sleep 5

cliclick m:1920,1080

# say "The Work has started operation."
