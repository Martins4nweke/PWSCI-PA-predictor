# app.py

import streamlit as st
import numpy as np

st.set_page_config(page_title="Physical Activity Predictor", layout="centered")

st.title("🧮 Probability of Being Physically Active")

st.markdown("""
This tool estimates the probability of a person being physically active based on:
- Age ≥ 50
- Gender (1 = female, 0 = male)
- Health Status (1 = good, 0 = not good)
""")

# Input fields
age_50 = st.selectbox("Is age ≥ 50?", ("No", "Yes"))
gender = st.selectbox("Gender", ("Male", "Female"))
health = st.selectbox("Health Status", ("Not good", "Good"))

# Convert to binary values
age_val = 1 if age_50 == "Yes" else 0
gender_val = 1 if gender == "Female" else 0
health_val = 1 if health == "Good" else 0

# Logistic regression equation
logit = 2.88 - 1.78 * age_val - 2.36 * gender_val + 2.22 * health_val
probability = 1 / (1 + np.exp(-logit))

# Show result
st.markdown(f"""
### ✅ Predicted Probability:
**{probability:.3f}** (or **{probability*100:.1f}%**)
""")

# Optional: Show the logit equation
st.caption(f"Logit = 2.88 - 1.78×({age_val}) - 2.36×({gender_val}) + 2.22×({health_val}) = {logit:.2f}")
