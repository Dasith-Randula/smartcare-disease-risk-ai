import streamlit as st
from utils.ui_utils import render_footer

st.title("About & Disclaimer")

st.markdown("""
<div class='glass-card'>
    <h3 class='insight-title'>About SmartCare AI</h3>
    <p>A machine-learning clinical decision-support prototype that classifies patient disease risk into Low, Medium, or High categories using SmartCare hospital data.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='glass-card'>
    <h3 class='insight-title'>Technology Stack</h3>
    <p>Python • Streamlit • Scikit-Learn • XGBoost • Pandas • Joblib</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='glass-card' style='text-align: center;'>
    <h3 class='insight-title'>System Flow</h3>
    <h5 class='flow-text'>Patient Data ➔ Preprocessing ➔ Machine Learning Model ➔ Disease Risk Prediction</h5>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='glass-card' style='border-left: 5px solid #E85D68;'>
    <h3 class='danger-title'>⚠️ Disclaimer</h3>
    <p>This system was developed for educational and research purposes. It is a decision-support prototype and must not replace professional medical diagnosis, treatment, or clinical judgement.</p>
</div>
""", unsafe_allow_html=True)

render_footer()