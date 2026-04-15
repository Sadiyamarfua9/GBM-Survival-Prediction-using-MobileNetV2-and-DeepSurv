import numpy as np

# Load tabular data
X_tab = np.load("X_tabular.npy")
time = np.load("time.npy")
event = np.load("event.npy")

# Load MRI data
X_mri = np.load("X_mri.npy")

print("Tabular shape:", X_tab.shape)
print("MRI shape:", X_mri.shape)

# Align sizes (IMPORTANT)
min_samples = min(len(X_tab), len(X_mri))

X_tab = X_tab[:min_samples]
X_mri = X_mri[:min_samples]
time = time[:min_samples]
event = event[:min_samples]

# Feature Fusion
X_fused = np.concatenate((X_tab, X_mri), axis=1)
print("Fused shape:", X_fused.shape)

# Save
np.save("X_fused.npy", X_fused)
np.save("time_fused.npy", time)
np.save("event_fused.npy", event)

print("✅ Feature fusion completed!")