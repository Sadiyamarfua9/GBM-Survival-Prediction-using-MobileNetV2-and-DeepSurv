import torch
import numpy as np
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
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

# Split into high/low risk
median_risk = np.median(risk)

high_risk = risk >= median_risk
low_risk = risk < median_risk

kmf = KaplanMeierFitter()

from lifelines.statistics import logrank_test

# Add after splitting groups
results = logrank_test(
    time[high_risk], time[low_risk],
    event[high_risk], event[low_risk]
)

print("p-value:", results.p_value)

print("High risk count:", sum(high_risk))
print("Low risk count:", sum(low_risk))

print("Median high:", np.median(time[high_risk]))
print("Median low:", np.median(time[low_risk]))

# Plot
plt.figure()

kmf.fit(time[high_risk], event[high_risk], label="High Risk")
kmf.plot()

kmf.fit(time[low_risk], event[low_risk], label="Low Risk")
kmf.plot()

plt.title("Kaplan-Meier Survival Curve")
plt.xlabel("Time (Months)")
plt.ylabel("Survival Probability")

plt.show()

