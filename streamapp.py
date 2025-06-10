import streamlit as st
import pandas as pd
import numpy as np
import joblib
from streamlit_lottie import st_lottie
import requests

model = joblib.load("xgb_diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

import json

def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_animation = load_lottie_file("robot.json")

st.set_page_config(page_title="GlucoBot", layout="centered", page_icon="🩺")

st.markdown("""
    <style>
    [data-testid="stForm"] {
    background-color: #B2C6D5; 
    padding: 20px; 
    border-radius: 10px; 
    }
            
    body {
        font-family: 'Segoe UI', sans-serif;
        [data-testid="stAppViewContainer"] {
        background-color: #2A4759;
    }
        
    .title {
        font-size: 30px;
        font-weight: 700;
        color: #F5ECD5;
    }
            
    .subtitle {
        font-size: 18px;
        color: #E7F2E4;
    }
            
    div[data-testid="stForm"] label,
    div[data-testid="stForm"] p {
        color: black;
    }
    
    st.form_submit_button {
        color : black;
    }
    
    [data-testid="stFormSubmitButton"] button p {
    color: black;
    }
    
    [data-testid="stFormSubmitButton"] button:hover {
    background-color: #e0e0e0;
    }
    
    .result {
        padding: 15px;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        color: black;
        background-color: #0E76A8;
    }
    
    </style>
""", unsafe_allow_html=True)

# Sidebar animation
with st.sidebar:
    st_lottie(lottie_animation, height=300, key="diabetes_anim")
    st.markdown("#### Understand Your Diabetes Risk, Effortlessly!")
    st.markdown("This tool uses machine learning to assess your diabetes risk based on health parameters. Designed for your convenience, " \
    "it's incredibly easy to use and provides fast insights into your health status")
    st.markdown("### 💡Quick Health Tips")
    st.markdown("- Prioritize a Balanced Diet")
    st.markdown("- Exercise Regularly")
    st.markdown("- Get Adequate Sleep")
    st.markdown("- Maintain a Healthy Weight")
    st.markdown("- Eat low-sugar, high-fiber food")

st.markdown('<p class="title">GlucoBot : AI-powered Diabetes Risk Predictor </p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enter the health details below:</p>', unsafe_allow_html=True)

# Form for user inputs
with st.form("diabetes_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.slider("Age", 1, 100, 30)
        height = st.slider("Height (cm)", 120.0, 200.0, 160.0)
        weight = st.slider("Weight (kg)", 30.0, 150.0, 70.0)
        hypertension = st.radio("Hypertension", ["No", "Yes"])
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        bmi = round(weight / ((height / 100) ** 2), 2)
        st.markdown(f"**Estimated BMI**: `{bmi}`", unsafe_allow_html=True)
        st.markdown(f"**Medical History**", unsafe_allow_html=True)
        # hypertension, heart_disease, smoking_history
        heart_disease = st.radio("Heart Disease", ["No", "Yes"])
        smoking_history = st.selectbox("Smoking History", ["never","No Info", "former", "current", "not current"])

        
        st.markdown(f"**Lab Results**", unsafe_allow_html=True)
        # HbA1c, glucose
        hba1c = st.number_input("HbA1c Level", min_value=3.0, max_value=15.0, step=0.1, value=5.5)
        glucose = st.number_input("Blood Glucose Level (mg/dL)", min_value=50, max_value=300, step=1, value=100)

    col_left, col_center, col_right = st.columns([1, 0.5, 1]) # Adjust ratios as needed
    with col_center:
        submitted = st.form_submit_button("🔍 Predict")


# Process inputs and predict
if submitted:
    gender_encoded = 1 if gender == "Male" else 0
    hypertension = 1 if hypertension == "Yes" else 0
    heart_disease = 1 if heart_disease == "Yes" else 0
    smoking_map = {"never": 0, "No Info": 1, "former": 2, "current": 3, "not current": 4}
    smoking_encoded = smoking_map[smoking_history]

    input_data = pd.DataFrame([[
        gender_encoded, age, height, weight, hypertension, heart_disease, smoking_encoded, hba1c, glucose
    ]], columns=[
        'gender', 'age', 'Height', 'Weight', 'hypertension', 'heart_disease',
        'smoking_history', 'HbA1c_level', 'blood_glucose_level'
    ])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.write("---")
    if prediction[0] == 1:
        st.markdown('<div class="result" style="background-color:#E74C3C;">⚠️ High Risk of Diabetes '
        '<p>It is crucial to consult a doctor without delay. A healthcare professional can perform definitive diagnostic tests and ' \
        'provide personalized advice. Ignoring a high risk can lead to the development of ' \
        'serious, irreversible complications. </p> </div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result" style="background-color:#2ECC71;">✅ Low Risk of Diabetes '
        '<p> The key is to maintain the healthy habits rigorously. Continue to eat a balanced diet, exercise regularly, ' \
        'manage stress, and get enough sleep. </p> </div>', unsafe_allow_html=True)
