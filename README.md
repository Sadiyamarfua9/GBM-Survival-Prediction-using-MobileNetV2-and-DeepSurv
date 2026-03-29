# GBM Survival Prediction using MobileNetV2 + DeepSurv

## Overview
This project predicts survival of Glioblastoma patients using:
- Clinical Data (Age, Gender, Therapy)
- Genomic Data (Gene Expression)
- MRI Images (BraTS)

## Pipeline
1. Clinical preprocessing
2. Genomic preprocessing
3. Data merging
4. MRI preprocessing
5. Feature extraction (MobileNetV2)
6. Feature-level fusion
7. Survival prediction (DeepSurv)