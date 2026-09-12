import streamlit as st
import pandas as pd
import joblib

model = joblib.load("SVM_Heart.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("Heart Stroke Prediction")
st.markdown("Provide the following Details")

age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex",['M','F'])
chestPain = st.selectbox("Chest Pain Type", ["ATA"], ["NAP"], ["TA"], ["ASY"])
restingBP = st.number_input("Resting BP (mm, Hg)",80, 200, 120)
cholestrol = st.number_input("Cholestrol (mg/dL)", 100, 600, 200)
fastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dL",[0, 1] )
restingECG = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
maxHR = st.slider("Max Heart Rate")
exercise_angina = st.selectboxO("Exercise-Induced Angina", ["Y", "N"])
old_peak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0 )
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):
    raw_input = {
        'Age' : age,
        'restingBP' : restingBP,
        'Cholestrol' : cholestrol,
        'FastingBS' : fastingBS,
        'MaxHR' : maxHR,
        'OldPeak' : old_peak,
        'Sex_' + sex: 1,
        'ChestPainType' + chestPain : 1,
        'RestingECG' + restingECG: 1,
        'ExerciseAngina' +  exercise_angina: 1,
        'ST_Slope' + st_slope: 1,
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
        st.success("Low Risk of Hear Disease")