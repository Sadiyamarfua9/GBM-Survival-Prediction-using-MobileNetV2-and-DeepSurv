import streamlit as st
import numpy as np
import torch
import cv2
import matplotlib.pyplot as plt

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load MobileNetV2
@st.cache_resource
def load_mobilenet():
    model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')
    return model

mobilenet = load_mobilenet()

# DeepSurv Model
class DeepSurv(torch.nn.Module):
    def __init__(self, input_dim):
        super(DeepSurv, self).__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(input_dim, 128),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.3),
            torch.nn.Linear(128, 64),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.3),
            torch.nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x)

# Load trained model
@st.cache_resource
def load_deepsurv():
    model = DeepSurv(input_dim=21800)  # your fused size
    model.load_state_dict(torch.load("models/deepsurv_fusion.pth", map_location='cpu'))
    model.eval()
    return model

model = load_deepsurv()

# MRI Feature Extraction
def extract_mri_features(img):
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    features = mobilenet.predict(img)
    return features.flatten()

# Survival Curve Function
def plot_survival_curve(risk):
    t = np.linspace(0, 24, 100)  # months
    scale = 10
    survival_prob = np.exp(-risk * t / scale)

    fig, ax = plt.subplots()
    ax.plot(t, survival_prob)
    ax.set_title("Estimated Survival Probability Curve")
    ax.set_xlabel("Time (months)")
    ax.set_ylabel("Survival Probability")
    ax.grid()

    return fig

# KM-style comparison (demo)
def plot_km_like():
    t = np.linspace(0, 24, 100)

    low_risk = np.exp(-0.1 * t)
    high_risk = np.exp(-0.5 * t)

    fig, ax = plt.subplots()
    ax.plot(t, low_risk, label="Low Risk")
    ax.plot(t, high_risk, label="High Risk")
    ax.legend()
    ax.set_title("Risk Group Survival Comparison")
    ax.set_xlabel("Time (months)")
    ax.set_ylabel("Survival Probability")
    ax.grid()

    return fig

# UI
st.title("🧠 Glioblastoma Survival Prediction")

st.write("Upload MRI slice (combined modality image) and enter clinical data")

# Upload MRI
uploaded_file = st.file_uploader("Upload MRI Image (PNG/JPG)", type=["png", "jpg", "jpeg"])

# Clinical inputs
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", ["Male", "Female"])

st.warning("⚠️ Genomic features are simulated (not provided by user)")

# Prediction Button
if st.button("Predict Survival Risk"):

    if uploaded_file is None:
        st.error("Please upload an MRI image")

    else:
        # Read image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        # Extract MRI features
        mri_features = extract_mri_features(img)

        # Clinical features
        sex_val = 1 if sex == "Male" else 0
        clinical_features = np.array([age, sex_val])

        # Genomic features (dummy)
        genomic_features = np.zeros(20518)  # Adjusted to match training dimensions

        # Combine all features
        combined = np.concatenate([clinical_features, genomic_features, mri_features])

        # Ensure correct size (pad if necessary)
        if len(combined) < 21800:
            combined = np.pad(combined, (0, 21800 - len(combined)), mode='constant', constant_values=0)
        else:
            combined = combined[:21800]

        X = torch.tensor(combined, dtype=torch.float32).unsqueeze(0)

        # Predict
        with torch.no_grad():
            risk = model(X).item()

        # Output
        st.success(f"Predicted Risk Score: {risk:.4f}")

        if risk > 0:
            st.error("High Risk Patient")
            st.warning("Likely shorter survival duration")
        else:
            st.success("Low Risk Patient")
            st.info("Likely longer survival duration")

        # Survival Curve
        st.subheader("📈 Survival Probability Curve")
        fig = plot_survival_curve(risk)
        st.pyplot(fig)

        # KM-style comparison
        st.subheader("📊 Risk Group Comparison")
        st.pyplot(plot_km_like())

        # Disclaimer
        st.warning("⚠️ Survival curves are approximate and for demonstration purposes only.")