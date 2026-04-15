import pandas as pd

# Load genomic data
genomic = pd.read_csv("datasets/tcga/data_mrna_seq_v2_rsem.txt", sep="\t")

# Remove unwanted column
if "Entrez_Gene_Id" in genomic.columns:
    genomic = genomic.drop("Entrez_Gene_Id", axis=1)

# Set gene names
genomic = genomic.set_index("Hugo_Symbol")

# Transpose
genomic = genomic.T

# Reset index
genomic.reset_index(inplace=True)

# Rename column
genomic.rename(columns={"index": "SAMPLE_ID"}, inplace=True)

# 🔥 KEEP ONLY TCGA rows
genomic = genomic[genomic["SAMPLE_ID"].str.startswith("TCGA")]


# 🔥 CONVERT TO PATIENT_ID

genomic["PATIENT_ID"] = genomic["SAMPLE_ID"].str[:12]

# Drop SAMPLE_ID
genomic = genomic.drop("SAMPLE_ID", axis=1)

# -----------------------------
# FINAL CHECK
# -----------------------------
print("Genomic IDs sample:")
print(genomic["PATIENT_ID"].head())

print("Shape:", genomic.shape)

# Save
genomic.to_csv("datasets/genomic_clean.csv", index=False)