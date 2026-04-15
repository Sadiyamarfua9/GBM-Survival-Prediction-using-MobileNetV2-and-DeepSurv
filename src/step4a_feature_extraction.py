import os
import numpy as np
import cv2
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

INPUT_PATH = "datasets/mri_processed"

model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

IMG_SIZE = 224

def extract_patient_features(patient_folder):
    features = []

    files = os.listdir(patient_folder)

    # 🔥 LIMIT slices per patient (VERY IMPORTANT)
    files = files[:50]   # use only 50 slices per patient

    for file in files:
        img_path = os.path.join(patient_folder, file)

        img = cv2.imread(img_path)
        if img is None:
            continue

        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        img = preprocess_input(img)

        img = np.expand_dims(img, axis=0)

        feat = model.predict(img, verbose=0)
        features.append(feat.flatten())

    if len(features) == 0:
        return None

    # Average pooling → patient-level feature
    return np.mean(features, axis=0)

X_mri = []
patient_ids = []

patients = os.listdir(INPUT_PATH)[:200]  # SAME LIMIT

for patient in patients:
    patient_folder = os.path.join(INPUT_PATH, patient)

    if not os.path.isdir(patient_folder):
        continue

    print("Extracting:", patient)

    feat = extract_patient_features(patient_folder)

    if feat is not None:
        X_mri.append(feat)
        patient_ids.append(patient)

X_mri = np.array(X_mri)

print("Final MRI feature shape:", X_mri.shape)

np.save("X_mri.npy", X_mri)
np.save("mri_patient_ids.npy", np.array(patient_ids))

print("✅ MRI feature extraction completed!")