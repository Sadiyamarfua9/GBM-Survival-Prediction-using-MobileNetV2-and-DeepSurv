import torch
import numpy as np
from step6_deepsurv_model import DeepSurv

# Cox loss
def cox_loss(risk, time, event):
    order = torch.argsort(time, descending=True)
    risk = risk[order]
    event = event[order]

    hazard_ratio = torch.exp(risk)
    log_risk = torch.log(torch.cumsum(hazard_ratio, dim=0))

    return -torch.mean((risk - log_risk) * event)

# Load data
X = np.load("X_fused.npy")
time = np.load("time_fused.npy")
event = np.load("event_fused.npy")

X = torch.tensor(X, dtype=torch.float32)
time = torch.tensor(time, dtype=torch.float32)
event = torch.tensor(event, dtype=torch.float32)

# Model
model = DeepSurv(input_dim=X.shape[1])
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training
for epoch in range(50):
    optimizer.zero_grad()

    risk = model(X).squeeze()
    loss = cox_loss(risk, time, event)

    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# Save
torch.save(model.state_dict(), "models/deepsurv_fusion.pth")

print("✅ Fusion model training completed!")