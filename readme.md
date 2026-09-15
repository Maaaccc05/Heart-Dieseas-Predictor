# Heart Disease Prediction

A machine learning web application that predicts the likelihood of heart disease based on patient health and clinical parameters.

The application uses a trained K-Nearest Neighbors (KNN) classification model and provides an interactive interface built with Streamlit.

## Features

- Interactive patient information form
- Heart disease prediction using KNN
- Data preprocessing using StandardScaler
- Categorical feature encoding
- Real-time prediction through a Streamlit interface
- Simple and user-friendly interface

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Joblib

## Machine Learning

The project uses a **K-Nearest Neighbors (KNN)** classification model.

The model takes various patient-related features such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope

The trained model and preprocessing files are stored using Joblib.
