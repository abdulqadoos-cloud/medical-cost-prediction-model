import streamlit as st
import pandas as pd
import joblib

# 1. Load your saved model and scaler
model = joblib.load('./models/medical_cost_gb_model.pkl')
scaler = joblib.load('./models/scaler.pkl')

# 2. Design the Web Page UI
st.title("🏥 Medical Cost Prediction App")
st.write("Enter patient details below to instantly predict their estimated insurance charges.")

# Create input widgets for the user
age = st.slider("Age", 18, 64, 30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI (Body Mass Index)", 10.0, 50.0, 25.0, step=0.1)
children = st.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])
smoker = st.selectbox("Smoker?", ["yes", "no"])
region = st.selectbox("Region", ["southeast", "southwest", "northwest", "northeast"])

# 3. Trigger prediction when the button is clicked
if st.button("Predict Charges"):
    
    # Put inputs into a DataFrame
    input_data = pd.DataFrame([{
        'age': age,
        'sex': sex,
        'bmi': bmi,
        'children': children,
        'smoker': smoker,
        'region': region
    }])
    
    # Encode categorical text values
    input_data['smoker_encoded'] = input_data['smoker'].map({'no': 0, 'yes': 1})
    input_data['sex_encoded'] = input_data['sex'].map({'female': 0, 'male': 1})
    
    # One-hot encode the region
    input_data = pd.get_dummies(input_data, columns=['region'], drop_first=True, dtype=int)
    
    # Ensure all columns match the exact feature set the model was trained on
    expected_cols = [
        'age', 'bmi', 'children', 'smoker_encoded', 'sex_encoded', 
        'region_northwest', 'region_southeast', 'region_southwest'
    ]
    
    for col in expected_cols:
        if col not in input_data.columns:
            input_data[col] = 0
    input_data = input_data[expected_cols]

    # Scale the numerical values using our saved scaler
    num_cols = ['age', 'bmi', 'children']
    input_data[num_cols] = scaler.transform(input_data[num_cols])
    
    # Make the prediction
    prediction = model.predict(input_data)[0]
    
    # Display the result nicely on the page
    st.success(f"Estimated Medical Charges: **${prediction:,.2f}**")