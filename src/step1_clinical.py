import pandas as pd

# Load clinical patient data
clinical = pd.read_csv(
    r"D:\Glioblastoma1\datasets\tcga\data_clinical_patient.txt",
    sep="\t",
    comment="#"
)

# Clean column names
clinical.columns = clinical.columns.str.strip()

print("Columns available:\n", clinical.columns)

# Select important features
clinical_selected = clinical[[
    "PATIENT_ID",
    "AGE",
    "SEX",
    "OS_MONTHS",
    "OS_STATUS"
]]

# Load sample file (for therapy)
sample = pd.read_csv(
    r"D:\Glioblastoma1\datasets\tcga\data_clinical_sample.txt",
    sep="\t",
    comment="#"
)

sample.columns = sample.columns.str.strip()

# Try to get therapy column (may vary)
if "THERAPY" in sample.columns:
    sample_selected = sample[["PATIENT_ID", "THERAPY"]]
else:
    sample_selected = sample[["PATIENT_ID"]]

# Merge clinical + therapy
clinical_final = pd.merge(
    clinical_selected,
    sample_selected,
    on="PATIENT_ID",
    how="left"
)

print("Clinical Data Shape:", clinical_final.shape)
print(clinical_final.head())

# Save
clinical_final.to_csv("datasets/clinical_clean.csv", index=False)