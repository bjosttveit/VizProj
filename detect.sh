#!/bin/sh

cd yolov5
python3 detect.py --source ../01_yolo/images/ --weights ../models/${1}.pt --img 1024 --project ../detect --name $1 --line-thickness 2 --exist-ok