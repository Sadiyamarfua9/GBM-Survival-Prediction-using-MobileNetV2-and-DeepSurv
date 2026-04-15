import torch
import numpy as np
from lifelines.utils import concordance_index
from step6_deepsurv_model import DeepSurv

# Load data
X = np.load("X_tabular.npy")
time = np.load("time.npy")
event = np.load("event.npy")

X_tensor = torch.tensor(X, dtype=torch.float32)

# Load model
model = DeepSurv(input_dim=X.shape[1])
model.load_state_dict(torch.load("models/deepsurv_tabular.pth"))
model.eval()

# Predict risk
with torch.no_grad():
    risk = model(X_tensor).numpy().flatten()

# Calculate C-index
c_index = concordance_index(time, -risk, event)

print("C-Index:", c_index)