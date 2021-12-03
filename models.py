import os
import wandb

api = wandb.Api()

runs = [
    {"artifact": "run_127f7oit_model:v0", "model": "n"},
    {"artifact": "run_uz30yl46_model:v0", "model": "n6"},
    {"artifact": "run_3b9by2ch_model:v0", "model": "s"},
    {"artifact": "run_2d0l7aln_model:v0", "model": "s6"},
    {"artifact": "run_2k6ao01f_model:v0", "model": "m"},
    {"artifact": "run_31kwfi31_model:v0", "model": "m6"},
    {"artifact": "run_1te89l0r_model:v0", "model": "l"},
    {"artifact": "run_2f5f27sr_model:v0", "model": "l6"},
    {"artifact": "run_co6roviu_model:v0", "model": "x"},
    {"artifact": "run_j7xy9jp0_model:v0", "model": "x6"},
]

if not os.path.exists('models'):
    os.makedirs('models')

for run in runs:
    print(f"Downloading {run['model']}...")
    api.artifact(f"TDT17/{run['artifact']}").download(root="./models")
    os.rename("models/best.pt", f"models/{run['model']}.pt")
