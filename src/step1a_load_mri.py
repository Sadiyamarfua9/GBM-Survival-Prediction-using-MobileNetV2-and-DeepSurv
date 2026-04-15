# Load all NIfTI files in a directory
def load_all_nii_in_dir(directory):
    nii_files = [f for f in os.listdir(directory) if f.endswith('.nii') or f.endswith('.nii.gz')]
    if not nii_files:
        print(f"No NIfTI files found in {directory}")
        return {}
    data_dict = {}
    for f in nii_files:
        file_path = os.path.join(directory, f)
        print(f"Loading: {file_path}")
        data_dict[f] = load_nii(file_path)
    return data_dict
import nibabel as nib
import os
def load_nii(path):
    print(f"Attempting to load: {path}")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Path does not exist or is not a file: {path}")
    if not (path.endswith('.nii') or path.endswith('.nii.gz')):
        raise ValueError(f"File does not have a valid NIfTI extension (.nii or .nii.gz): {path}")
    img = nib.load(path)
    data = img.get_fdata()
    return data

# Example: load all NIfTI files in a directory
example_dir = r"datasets/braTS/BraTS2021_00495"
all_volumes = load_all_nii_in_dir(example_dir)

def load_modality(path, keyword):
    for file in os.listdir(path):
        if keyword in file.lower() and file.endswith(".nii.gz"):
            return nib.load(os.path.join(path, file)).get_fdata()
    return None
for fname, arr in all_volumes.items():
    print(f"{fname}: shape {arr.shape}")