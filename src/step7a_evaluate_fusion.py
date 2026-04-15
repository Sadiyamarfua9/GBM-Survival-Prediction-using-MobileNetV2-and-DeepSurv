import torch
import numpy as np
from lifelines.utils import concordance_index
from step6_deepsurv_model import DeepSurv

# Load
X = np.load("X_fused.npy")
time = np.load("time_fused.npy")
event = np.load("event_fused.npy")

X_tensor = torch.tensor(X, dtype=torch.float32)

# Model
model = DeepSurv(input_dim=X.shape[1])
model.load_state_dict(torch.load("models/deepsurv_fusion.pth"))
model.eval()

# Predict
with torch.no_grad():
    risk = model(X_tensor).numpy().flatten()

# C-index
c_index = concordance_index(time, -risk, event)

print("Final C-Index:", c_index)