import os
import cv2

INPUT_PATH = "datasets/mri_slices"
OUTPUT_PATH = "datasets/mri_processed"

IMG_SIZE = 224
def preprocess_patient(patient):
    input_folder = os.path.join(INPUT_PATH, patient)
    output_folder = os.path.join(OUTPUT_PATH, patient)

    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)

        img = cv2.imread(input_path)

        if img is None:
            continue

        # Resize
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

        # Normalize
        img = img / 255.0

        # Save back (convert to uint8)
        cv2.imwrite(output_path, (img * 255).astype("uint8"))

# 🔥 Process LIMITED patients to avoid overload
patients = os.listdir(INPUT_PATH)[:200]  # CHANGE if needed

for patient in patients:
    print("Processing:", patient)
    preprocess_patient(patient)

print("✅ MRI preprocessing completed!")