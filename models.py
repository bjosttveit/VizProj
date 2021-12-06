import os
import wandb

api = wandb.Api()

runs = [
    {"artifact": "run_2q343zly_model:v0", "model": "n"},
    {"artifact": "run_1bv2ss4i_model:v0", "model": "n6"},
    {"artifact": "run_1q5qb4h3_model:v0", "model": "s"},
    {"artifact": "run_qmpgajz4_model:v0", "model": "s6"},
    {"artifact": "run_1brla0sx_model:v0", "model": "m"},
    {"artifact": "run_2pjojkr4_model:v0", "model": "m6"},
    {"artifact": "run_1e8mqw56_model:v0", "model": "l"},
    {"artifact": "run_38d0005f_model:v0", "model": "l6"},
    {"artifact": "run_2x2i1j91_model:v0", "model": "x"},
    {"artifact": "run_1nfbf38q_model:v0", "model": "x6"},
]

if not os.path.exists('models'):
    os.makedirs('models')

for run in runs:
    print(f"Downloading {run['model']}...")
    api.artifact(f"TDT17/{run['artifact']}").download(root="./models")
    os.rename("models/best.pt", f"models/{run['model']}.pt")
