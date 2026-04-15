import os
import cv2
import numpy as np
import nibabel as nib

DATASET_PATH = "datasets/braTS/BraTS2021_Training_Data"
OUTPUT_PATH = "datasets/mri_slices"

def load_modality(patient_folder, keyword):
    for file in os.listdir(patient_folder):
        if keyword in file.lower():
            return nib.load(os.path.join(patient_folder, file)).get_fdata()
    return None

def extract_slices(patient_folder):
    patient_id = os.path.basename(patient_folder)

    flair = load_modality(patient_folder, "flair")
    t1ce = load_modality(patient_folder, "t1ce")
    t2 = load_modality(patient_folder, "t2")

    if flair is None or t1ce is None or t2 is None:
        print("Skipping:", patient_id)
        return

    patient_output = os.path.join(OUTPUT_PATH, patient_id)
    os.makedirs(patient_output, exist_ok=True)

    for i in range(flair.shape[2]):

        # 🔥 MULTIMODAL → RGB MAPPING
        slice_img = np.stack([
            flair[:, :, i],   # R
            t1ce[:, :, i],    # G
            t2[:, :, i]       # B
        ], axis=-1)

        # Normalize
        slice_img = cv2.normalize(slice_img, None, 0, 255, cv2.NORM_MINMAX)
        slice_img = slice_img.astype(np.uint8)

        cv2.imwrite(f"{patient_output}/slice_{i}.png", slice_img)

# Loop all patients
for patient in os.listdir(DATASET_PATH):
    patient_path = os.path.join(DATASET_PATH, patient)

    if os.path.isdir(patient_path):
        print("Processing:", patient)
        extract_slices(patient_path)

print("✅ Multimodal slice extraction completed!")