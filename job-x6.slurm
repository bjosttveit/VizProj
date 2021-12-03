#!/bin/sh
#SBATCH --partition=GPUQ
#SBATCH --account=ie-idi
#SBATCH --time=18:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:V100:2
#SBATCH --cpus-per-task=24
#SBATCH --mem=16G
#SBATCH --job-name="AV_YOLO"
#SBATCH --output=av_yolo_x6.out
#SBATCH --mail-user=bjornar.osttveit@ntnu.no
#SBATCH --mail-type=NONE


cd ${SLURM_SUBMIT_DIR}/yolov5

module purge
module load Python/3.8.6-GCCcore-10.2.0

pip3 install -r requirements.txt --user -q
pip3 install wandb --user -q

#python3 train.py --project TDT17 --name X6 --exist-ok --batch 4 --device 0 --epochs 1000 --data ../dataset/dataset.yaml --weights yolov5x6.pt --img 1024
python3 -m torch.distributed.launch --nproc_per_node=2 train.py --project TDT17 --name X6 --exist-ok --batch 8 --device 0,1 --workers 16 --epochs 1000 --data ../dataset/dataset.yaml --weights yolov5x6.pt --img 1024
