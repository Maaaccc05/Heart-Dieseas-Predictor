import streamlit as st
import pandas as pd
import joblib

model = joblib.load("SVM_Heart.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("Heart Stroke Prediction")
st.markdown("Provide the following Details")

age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex",['Male','Female'])
chestPain = st.selectbox("Chest Pain Type", ["ATA"], ["NAP"], ["TA"], ["ASY"])
restingBP = st.number_input("Resting BP (mm, Hg)",80, 200, 120)
cholestrol = st.number_input("Cholestrol (mg/dL)", 100, 600, 200)
fastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dL",[0, 1] )
restingECG = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
maxHR = st.slider("Max Heart Rate")
exercise_angina = st.selectboxO("Exercise-Induced Angina", ["Y", "N"])
old_peak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0 )
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])
