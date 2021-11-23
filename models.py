import os
import wandb

api = wandb.Api()

runs = [
    {"artifact": "run_1ee986s2_model:v0", "model": "n"},
    {"artifact": "run_3u9pn5lp_model:v0", "model": "n6"},
    {"artifact": "run_q6s5egmt_model:v0", "model": "s"},
    {"artifact": "run_3d1auekm_model:v0", "model": "s6"},
    {"artifact": "run_2lc4ubop_model:v0", "model": "m"},
    {"artifact": "run_37kan8fz_model:v0", "model": "m6"},
    {"artifact": "run_129dpchz_model:v0", "model": "l"},
    {"artifact": "run_1x8y5m2a_model:v0", "model": "l6"},
    #{"artifact": "run_---_model:v0", "model": "x"},
    #{"artifact": "run_---_model:v0", "model": "x6"},
]

if not os.path.exists('models'):
    os.makedirs('models')

for run in runs:
    print(f"Downloading {run['model']}...")
    api.artifact(f"TDT17/{run['artifact']}").download(root="./models")
    os.rename("models/best.pt", f"models/{run['model']}.pt")
