# 🧠 Brain Tumor Detection System

An AI-powered web application that identifies brain tumors in MRI scans using Deep Learning (CNNs). This system provides real-time classification to assist in medical diagnostics.

## 🚀 Key Features
- **Accurate Classification**: Detects 4 categories: Glioma, Meningioma, Pituitary, and No Tumor.
- **Instant Inference**: Upload an MRI scan and receive predictions with confidence scores.
- **Web Interface**: Clean, user-friendly dashboard built with Flask.

## 📸 Project Showcase
[Insert a screenshot of your app here]
*(Take a screenshot of your browser window while your app is running and save it in your project as `showcase.png`)*
![Project Interface](showcase.png)

## 🛠 Tech Stack
- **AI/ML**: TensorFlow, Keras, Pillow (Image Preprocessing)
- **Web**: Flask, HTML5, CSS3
- **Tools**: Git, Git LFS (Large File Storage)

## 📖 How to Run Locally
1. **Clone the repo:**
   `git clone https://github.com/Dee7anjali/Brain-Tumor-Detection.git`
2. **Setup virtual environment:**
   `python -m venv .venv`
   `.\.venv\Scripts\Activate.ps1`
3. **Install dependencies:**
   `pip install -r requirements.txt`
4. **Run the server:**
   `python main.py`
5. **Access the app:**
   Open `http://127.0.0.1:5000` in your browser.

## 🔬 How it Works

1. **Preprocessing**: Images are resized and normalized using Pillow.
2. **Prediction**: The CNN model (trained on MRI datasets) analyzes the input and returns a probability vector.
3. **Output**: The Flask backend maps the result to one of the 4 tumor categories and renders the confidence level.

## 👤 Credits
- Developed by: Deepanjali Mohanty
