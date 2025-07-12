# app.py

import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Physical Activity Probability", layout="centered")

# Title and description
st.title("🏃‍♂️ PWSCI Physical Activity Probability Estimator")
st.markdown("Estimate the likelihood of being physically active based on age, gender, and health status.")

st.divider()

# Input section
st.header("🧾 Input Parameters")

col1, col2, col3 = st.columns(3)
with col1:
    age_50 = st.selectbox("Is age ≥ 50?", ("No", "Yes"))
with col2:
    gender = st.selectbox("Gender", ("Male", "Female"))
with col3:
    health = st.selectbox("Health Status", ("Not good", "Good"))

# Convert inputs to binary
age_val = 1 if age_50 == "Yes" else 0
gender_val = 1 if gender == "Female" else 0
health_val = 1 if health == "Good" else 0

# Logistic regression formula
logit = 2.88 - 1.78 * age_val - 2.36 * gender_val + 2.22 * health_val
probability = 1 / (1 + np.exp(-logit))

# Output section
st.header("📊 Prediction Result")
st.markdown(f"### ✅ Probability of Being Physically Active: **{probability:.3f}** ({probability*100:.1f}%)")

st.progress(min(probability, 1.0), text=f"{probability*100:.1f}%")

st.caption(f"Logit = 2.88 - 1.78×({age_val}) - 2.36×({gender_val}) + 2.22×({health_val}) = {logit:.2f}")

# 📌 Interpretation logic
st.header("🧠 Interpretation")

if probability >= 0.80:
    level = "a **high** probability"
    tone = "This person is very likely to be physically active"
elif 0.5 <= probability < 0.80:
    level = "a **moderate** probability"
    tone = "This person has a fair chance of being physically active"
else:
    level = "a **low** probability"
    tone = "This person is unlikely to be physically active"

reasoning = []
if age_val == 0:
    reasoning.append("younger than 50")
else:
    reasoning.append("aged 50 or older")
if gender_val == 0:
    reasoning.append("male")
else:
    reasoning.append("female")
if health_val == 1:
    reasoning.append("in good health")
else:
    reasoning.append("not in good health")

st.markdown(f"""
This individual has {level} of being physically active.  
**{tone}**, likely because the person is **{', '.join(reasoning)}**.
""")

# Create DataFrame for download
results_df = pd.DataFrame({
    "Age ≥ 50": [age_50],
    "Gender": [gender],
    "Health Status": [health],
    "Logit": [round(logit, 2)],
    "Probability": [round(probability, 3)]
})

# CSV download
st.download_button(
    label="📥 Download Prediction as CSV",
    data=results_df.to_csv(index=False),
    file_name="prediction_result.csv",
    mime="text/csv"
)

# Footer
st.divider()
st.markdown("🔧 Developed using [Streamlit](https://streamlit.io).")
