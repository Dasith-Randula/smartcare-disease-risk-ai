import streamlit as st
from utils.ui_utils import render_footer

st.markdown("<h4 class='section-eyebrow'>AI-Powered Healthcare Intelligence</h4>", unsafe_allow_html=True)
st.title("SmartCare AI")
st.subheader("Disease Risk Prediction System")

k1, k2, k3, k4 = st.columns(4)
k1.markdown("<div class='kpi-card kpi-blue'><div class='kpi-label'>Total Patients</div><div class='kpi-value'>1,644+</div></div>", unsafe_allow_html=True)
k2.markdown("<div class='kpi-card kpi-pink'><div class='kpi-label'>Old Patients</div><div class='kpi-value'>300+</div></div>", unsafe_allow_html=True)
k3.markdown("<div class='kpi-card kpi-green'><div class='kpi-label'>New Patients</div><div class='kpi-value'>100+</div></div>", unsafe_allow_html=True)
k4.markdown("<div class='kpi-card kpi-amber'><div class='kpi-label'>Appointments</div><div class='kpi-value'>355+</div></div>", unsafe_allow_html=True)

col1, col2 = st.columns([0.6, 0.4])

with col1:
    st.markdown("""
    <div class='surface-card'>
    A machine-learning clinical decision-support prototype that classifies patient 
    disease risk into Low, Medium, or High categories using SmartCare hospital data.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Predict Patient Risk", type="primary" ):
        st.switch_page("views/patient_prediction.py")

with col2:
    st.markdown("""
    <div class="med-mark-wrap">
        <div class="med-mark-dot dot-a"></div>
        <div class="med-mark-dot dot-b"></div>
        <div class="med-mark-dot dot-c"></div>
        <div class="med-mark-core">✚</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### System Metrics")
m1, m2, m3 = st.columns(3)
m1.markdown("<div class='glass-card'><h2>🏥 1,000</h2><p class='muted-text'>Patient Records</p></div>", unsafe_allow_html=True)
m2.markdown("<div class='glass-card'><h2>🧠 4</h2><p class='muted-text'>Base ML Models</p></div>", unsafe_allow_html=True)
m3.markdown("<div class='glass-card'><h2>⚡ 94.5%</h2><p class='muted-text'>Best Accuracy</p></div>", unsafe_allow_html=True)

render_footer()