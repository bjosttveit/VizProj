#!/bin/sh

mkdir -p tests

cd yolov5
python3 val.py --data ../dataset/dataset.yaml --weights ../models/${1}.pt --project ../tests --name ${1} --exist-ok --batch-size 1 --task=test --save-txt --save-conf --img 1024
