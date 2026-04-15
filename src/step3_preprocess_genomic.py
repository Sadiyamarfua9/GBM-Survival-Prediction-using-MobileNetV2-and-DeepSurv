import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler

# Load genomic
genomic = pd.read_csv("datasets/genomic_clean.csv")

# Separate patient ID
patient_ids = genomic["PATIENT_ID"]
genomic = genomic.drop("PATIENT_ID", axis=1)

# Fill missing values
genomic = genomic.fillna(0)

# Scale
scaler = StandardScaler()
genomic_scaled = scaler.fit_transform(genomic)

# Feature selection
selector = VarianceThreshold(threshold=0.01)
genomic_selected = selector.fit_transform(genomic_scaled)

print("Reduced genomic shape:", genomic_selected.shape)

# Convert back to DataFrame
genomic_selected = pd.DataFrame(genomic_selected)

# Add patient ID back
genomic_selected.insert(0, "PATIENT_ID", patient_ids)

# Save
genomic_selected.to_csv("datasets/genomic_processed.csv", index=False)