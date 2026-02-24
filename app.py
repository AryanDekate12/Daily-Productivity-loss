import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("ridge_productivity_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Daily Productivity Loss Predictor")
st.write("Predict productivity loss (in hours) based on daily habits")

# User inputs
social = st.number_input("Social Media Hours", 0.0, 24.0, step=0.1)
screen = st.number_input("Screen Time Hours", 0.0, 24.0, step=0.1)
notif = st.number_input("Notifications Count", 0, 500)
sleep = st.number_input("Sleep Hours", 0.0, 24.0, step=0.1)
study = st.number_input("Study Hours", 0.0, 24.0, step=0.1)
breaks = st.number_input("Break Hours", 0.0, 24.0, step=0.1)
deadline = st.number_input("Days to Deadline", 0, 90)
mood = st.slider("Mood Score", 1, 10)

# Prediction
if st.button("Predict Productivity Loss"):
    input_data = np.array([[social, screen, notif, sleep, study, breaks, deadline, mood]])
    prediction = model.predict(input_data)

    st.success(f"Estimated Productivity Loss: {prediction[0]:.2f} hours")
