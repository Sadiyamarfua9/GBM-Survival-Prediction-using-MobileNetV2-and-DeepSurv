import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load merged dataset
df = pd.read_csv("datasets/clinical_genomic.csv")

print("Initial shape:", df.shape)

# Remove unwanted and unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Drop ID columns
df = df.drop(["PATIENT_ID", "SAMPLE_ID"], axis=1, errors='ignore')

# Encode categorical variables
le = LabelEncoder()

categorical_cols = [
    "SEX",
    "MGMT_STATUS",
    "IDH1_MUTATION",
    "METHYLATION_STATUS",
    "EXPRESSION_SUBTYPE"
]

for col in categorical_cols:
    if col in df.columns:
        df[col] = le.fit_transform(df[col].astype(str))

# Survival columns
# Time (months)
time = df["OS_MONTHS"].values

# Event (1 = deceased, 0 = alive)
event = df["OS_STATUS"].apply(
    lambda x: 1 if "DECEASED" in str(x) else 0
).values

# Drop survival columns from features
df = df.drop(["OS_MONTHS", "OS_STATUS"], axis=1)

# Handle missing values
df = df.fillna(0)

# Fix fragmentation warning (optional but good)
df = df.copy()

# Feature scaling
scaler = StandardScaler()
X = scaler.fit_transform(df)

print("Final feature shape:", X.shape)

# Save outputs
np.save("X_tabular.npy", X)
np.save("time.npy", time)
np.save("event.npy", event)

print("✅ Step 5 completed successfully!")