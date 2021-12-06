#!/bin/sh

# Uncomment when running on IDUN
#module purge
#module load Python/3.8.6-GCCcore-10.2.0

kaggle datasets download -d bjosttveit/tdt17avcombined
rm -rf dataset/images dataset/labels
unzip -o tdt17avcombined.zip -d dataset
rm tdt17avcombined.zip
