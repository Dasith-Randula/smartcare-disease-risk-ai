import streamlit as st
from utils.ui_utils import render_footer, render_page_header

render_page_header("About the System", "AI-driven clinical decision support for safer, faster risk triage.", eyebrow="SmartCare AI", icon="info")

st.markdown(
    """
    <div class='glass-card' style='padding: 1.3rem 1.4rem; border-left: 5px solid var(--primary); border-radius: 22px;'>
        <h3 style='margin: 0 0 0.6rem;'>About SmartCare AI</h3>
        <p style='margin: 0; color: var(--text-secondary);'>A machine-learning clinical decision-support prototype that classifies patient disease risk into Low, Medium, or High categories using SmartCare hospital data.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='glass-card' style='padding: 1.3rem 1.4rem; border-radius: 22px;'>
        <h3 style='margin: 0 0 0.9rem;'>Technology Stack</h3>
        <div style='display: flex; flex-wrap: wrap; gap: 0.55rem;'>
            <span style='padding: 0.46rem 0.75rem; border-radius: 999px; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.14); font-weight: 600;'>Python</span>
            <span style='padding: 0.46rem 0.75rem; border-radius: 999px; background: rgba(5, 150, 105, 0.08); border: 1px solid rgba(5, 150, 105, 0.14); font-weight: 600;'>Streamlit</span>
            <span style='padding: 0.46rem 0.75rem; border-radius: 999px; background: rgba(40, 184, 213, 0.08); border: 1px solid rgba(40, 184, 213, 0.14); font-weight: 600;'>Scikit-Learn</span>
            <span style='padding: 0.46rem 0.75rem; border-radius: 999px; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.14); font-weight: 600;'>Pandas</span>
            <span style='padding: 0.46rem 0.75rem; border-radius: 999px; background: rgba(5, 150, 105, 0.08); border: 1px solid rgba(5, 150, 105, 0.14); font-weight: 600;'>Joblib</span>
            <span style='padding: 0.46rem 0.75rem; border-radius: 999px; background: rgba(40, 184, 213, 0.08); border: 1px solid rgba(40, 184, 213, 0.14); font-weight: 600;'>XGBoost</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

flow_cols = st.columns(4)
labels = ["Patient Data", "Preprocessing", "ML Model", "Risk Prediction"]
for idx, label in enumerate(labels):
    with flow_cols[idx]:
        st.markdown(
            f"""
            <div class='glass-card' style='padding: 1rem; text-align: center; border-radius: 18px; min-height: 110px; display: flex; flex-direction: column; justify-content: center;'>
                <div style='font-size: 0.74rem; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; color: var(--primary);'>Step {idx+1}</div>
                <div style='font-size: 1.05rem; font-weight: 700; margin-top: 0.5rem;'>{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class='glass-card' style='border-left: 5px solid #F4A62A; background: rgba(244,166,42,0.05); border-radius: 22px; margin-top: 1.3rem;'>
        <h3 style='margin: 0 0 0.6rem; color: #C67B00;'>Disclaimer</h3>
        <p style='margin: 0; color: var(--text-secondary);'>This system was developed for educational and research purposes. It is a decision-support prototype and must not replace professional medical diagnosis, treatment, or clinical judgement.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

render_footer()



