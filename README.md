YOLOv5: <https://github.com/ultralytics/yolov5>
# Autonomous vehicle object detection with YOLOv5 🚀
Miniproject for TDT17 Fall 2021

## Prerequisites
- Kaggle: `pip3 install kaggle` (follow official instructions for authentication)
- Weights & biases: `pip3 install wandb` (follow official instructions for authentication)

## Install YOLOv5 into the root dir.
1. Clone the repo: `git clone https://github.com/ultralytics/yolov5.git`.
2. Install the necessary dependencies: `cd yolov5` & `pip3 install -r requirements.txt`.

## Download the dataset
Dataset can be found on kaggle: <https://www.kaggle.com/bjosttveit/tdt17avcombined>

Run `./data.sh` to download the training data from kaggle.

## Download the models
Models can be found on weights and biases: <https://wandb.ai/bjosttveit/TDT17>

Run `python3 models.py` to download the custom models trained on the data.

## Detect
To produce frames with bounding boxes overlaid, run: `./detect.sh [n|n6|s|s6|m|m6|l|l6|x|x6]`.

## Test performance
Run `./test.sh [n|n6|s|s6|m|m6|l|l6|x|x6]` to evaluate a model on the test set.
