import streamlit as st
import pandas as pd
import joblib

model = joblib.load("KNN_Heart.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("Heart Stroke Prediction")
st.markdown("Provide the following Details")

age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chestPain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
restingBP = st.number_input("Resting BP (mm, Hg)", 80, 200, 120)
cholestrol = st.number_input("Cholestrol (mg/dL)", 100, 600, 200)
fastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
restingECG = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
maxHR = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
old_peak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):
    raw_input = {
        "Age": age,
        "RestingBP": restingBP,
        "Cholesterol": cholestrol,
        "FastingBS": fastingBS,
        "MaxHR": maxHR,
        "Oldpeak": old_peak,
        "Sex_M": 1 if sex == "M" else 0,
        "ChestPainType_ATA": 1 if chestPain == "ATA" else 0,
        "ChestPainType_NAP": 1 if chestPain == "NAP" else 0,
        "ChestPainType_TA": 1 if chestPain == "TA" else 0,
        "RestingECG_Normal": 1 if restingECG == "Normal" else 0,
        "RestingECG_ST": 1 if restingECG == "ST" else 0,
        "ExerciseAngina_Y": 1 if exercise_angina == "Y" else 0,
        "ST_Slope_Up": 1 if st_slope == "Up" else 0,
        "ST_Slope_Flat": 1 if st_slope == "Flat" else 0,
        "Age_Young": 1 if age < 40 else 0,
        "Age_Middle": 1 if 40 <= age < 60 else 0,
        "Age_Senior": 1 if age >= 60 else 0,
        "MaxHR_Age_ratio": maxHR / age,
        "HighCholesterol": 1 if cholestrol > 240 else 0,
        "Age^2": age ** 2,
        "Age RestingBP": age * restingBP,
        "Age Cholesterol": age * cholestrol,
        "Age MaxHR": age * maxHR,
        "Age Oldpeak": age * old_peak,
        "RestingBP^2": restingBP ** 2,
        "RestingBP Cholesterol": restingBP * cholestrol,
        "RestingBP MaxHR": restingBP * maxHR,
        "RestingBP Oldpeak": restingBP * old_peak,
        "Cholesterol^2": cholestrol ** 2,
        "Cholesterol MaxHR": cholestrol * maxHR,
        "Cholesterol Oldpeak": cholestrol * old_peak,
        "MaxHR^2": maxHR ** 2,
        "MaxHR Oldpeak": maxHR * old_peak,
        "Oldpeak^2": old_peak ** 2
    }

    input_df = pd.DataFrame([raw_input])

    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("High Risk of Heart Disease")
    else:
        st.success("Low Risk of Heart Disease")