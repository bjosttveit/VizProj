#!/bin/sh

cd yolov5
python3 detect.py --source ../10_yolo/images/ --weights ../models/${1}.pt --img 1024 --project ../detect --name $1 --line-thickness 2 --exist-ok --conf-thres 0.3
