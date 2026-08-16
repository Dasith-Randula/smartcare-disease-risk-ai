import streamlit as st
from utils.ui_utils import render_footer

st.markdown("<h4 style='color: #7e948a;'>AI-Powered Healthcare Intelligence</h4>", unsafe_allow_html=True)
st.title("SmartCare AI")
st.subheader("Disease Risk Prediction System")

col1, col2 = st.columns([0.6, 0.4])

with col1:
    st.markdown("""
    <div class='glass-card'>
    A machine-learning clinical decision-support prototype that classifies patient 
    disease risk into Low, Medium, or High categories using SmartCare hospital data.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Predict Patient Risk", type="primary"):
        st.switch_page("views/patient_prediction.py")

with col2:
    st.markdown("""
    <div class="orb-container">
        <div class="orb">✚</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### System Metrics")
m1, m2, m3 = st.columns(3)
m1.markdown("<div class='glass-card'><h2>🏥 1,000</h2><p>Patient Records</p></div>", unsafe_allow_html=True)
m2.markdown("<div class='glass-card'><h2>🧠 4</h2><p>Base ML Models</p></div>", unsafe_allow_html=True)
m3.markdown("<div class='glass-card'><h2>⚡ 94.5%</h2><p>Best Accuracy</p></div>", unsafe_allow_html=True)

render_footer()