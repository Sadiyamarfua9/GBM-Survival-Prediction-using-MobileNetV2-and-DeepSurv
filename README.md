# 🧠 Glioblastoma Survival Prediction System 🩺📊

A multimodal AI-based system to predict survival risk in Glioblastoma (GBM) patients using **clinical, genomic, and MRI data**.
<<<<<<< HEAD

---

## 🌐 Project Overview

This project integrates deep learning and survival analysis to provide accurate prognosis for GBM patients.

It combines:
- 📊 Clinical data (Age, Sex, Survival)
- 🧬 Genomic data (~20,000 genes)
- 🧠 MRI images (BraTS dataset)

---

## 🚀 Features

✔️ Multimodal data integration (Clinical + Genomic + MRI)  
✔️ Deep learning-based MRI feature extraction (MobileNetV2)  
✔️ Survival prediction using DeepSurv  
✔️ Kaplan-Meier survival analysis  
✔️ Risk stratification (High-risk / Low-risk)

---

## 🛠️ Tech Stack

**Frontend (Optional):** Streamlit  
**Backend:** Python  
**Libraries:** Pandas, NumPy, PyTorch, TensorFlow/Keras  
**Models:**
- MobileNetV2 (Feature Extraction)
- DeepSurv (Survival Prediction)

---

## 📂 Datasets Used

📊 **TCGA-GBM (Clinical + Genomic)**  
🔗 https://www.cbioportal.org/

🧠 **BraTS 2021 (MRI Dataset)**  
🔗 https://www.med.upenn.edu/cbica/brats2021/data.html

---

## ⚙️ Project Pipeline

1️⃣ Load Clinical & Genomic Data  
2️⃣ Preprocess and Merge Data  
3️⃣ Prepare Survival Data (Time + Event)  
4️⃣ Load MRI Scans (BraTS)  
5️⃣ Extract MRI Slices  
6️⃣ Feature Extraction (MobileNetV2 → 1280 features)  
7️⃣ Feature Fusion (Multimodal Integration)  
8️⃣ Train DeepSurv Model  
9️⃣ Evaluate using C-index  
🔟 Kaplan-Meier Survival Analysis  

---

## 📊 Results

| Metric | Value |
|------|------|
| Patients | 152 |
| MRI Slices | ~193,905 |
| Features | ~21,800 |
| C-Index | **0.89** |
| p-value | **< 0.001** |

---

🌟 How to Run Locally
### 1️⃣ Clone the Repository
git clone https://github.com/your-username/GBM-survival-prediction.git
cd GBM-survival-prediction

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt
=======

---

## 🌐 Project Overview

This project integrates deep learning and survival analysis to provide accurate prognosis for GBM patients.

It combines:
- 📊 Clinical data (Age, Sex, Survival)
- 🧬 Genomic data (~20,000 genes)
- 🧠 MRI images (BraTS dataset)

---

## 🚀 Features

✔️ Multimodal data integration (Clinical + Genomic + MRI)  
✔️ Deep learning-based MRI feature extraction (MobileNetV2)  
✔️ Survival prediction using DeepSurv  
✔️ Kaplan-Meier survival analysis  
✔️ Risk stratification (High-risk / Low-risk)

---

## 🛠️ Tech Stack

**Frontend (Optional):** Streamlit  
**Backend:** Python  
**Libraries:** Pandas, NumPy, PyTorch, TensorFlow/Keras  
**Models:**
- MobileNetV2 (Feature Extraction)
- DeepSurv (Survival Prediction)

---

## 📂 Datasets Used

📊 **TCGA-GBM (Clinical + Genomic)**  
🔗 https://www.cbioportal.org/

🧠 **BraTS 2021 (MRI Dataset)**  
🔗 https://www.med.upenn.edu/cbica/brats2021/data.html

---

## ⚙️ Project Pipeline

1️⃣ Load Clinical & Genomic Data  
2️⃣ Preprocess and Merge Data  
3️⃣ Prepare Survival Data (Time + Event)  
4️⃣ Load MRI Scans (BraTS)  
5️⃣ Extract MRI Slices  
6️⃣ Feature Extraction (MobileNetV2 → 1280 features)  
7️⃣ Feature Fusion (Multimodal Integration)  
8️⃣ Train DeepSurv Model  
9️⃣ Evaluate using C-index  
🔟 Kaplan-Meier Survival Analysis  

---

## 📊 Results

| Metric | Value |
|------|------|
| Patients | 152 |
| MRI Slices | ~193,905 |
| Features | ~21,800 |
| C-Index | **0.89** |
| p-value | **< 0.001** |

---

## 🌟 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/GBM-survival-prediction.git
cd GBM-survival-prediction

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

>>>>>>> 022419d479b3b51b189c2535467ad9bbc3f97dd0
