import pandas as pd

# Load both
clinical = pd.read_csv("datasets/clinical_clean.csv")
genomic = pd.read_csv("datasets/genomic_clean.csv")

# Merge on PATIENT_ID
merged = pd.merge(clinical, genomic, on="PATIENT_ID", how="inner")
print("Merged shape:", merged.shape)
print("Clinical IDs sample:", clinical["PATIENT_ID"].head())
print("Genomic IDs sample:", genomic["PATIENT_ID"].head())
# Save
merged.to_csv("datasets/clinical_genomic.csv", index=False)