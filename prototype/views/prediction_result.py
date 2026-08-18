import streamlit as st
from utils.ui_utils import get_icon_svg, render_footer, render_page_header

render_page_header("Prediction Result", "Clinical decision support output for the selected patient profile.", eyebrow="Predictive Output", icon="health_and_safety")

if 'last_prediction' not in st.session_state:
    st.markdown(
        f"""
        <div class='glass-card' style='padding: 2rem 1.5rem; text-align: center;'>
            <div style='display: inline-flex; align-items: center; justify-content: center; width: 68px; height: 68px; border-radius: 50%; background: linear-gradient(135deg, rgba(16,185,129,0.12), rgba(5,150,105,0.08)); margin-bottom: 1rem;'>{get_icon_svg('info', 30, 'var(--primary)')}</div>
            <h3 style='margin: 0 0 0.6rem;'>No prediction is available yet.</h3>
            <p style='margin: 0; color: var(--text-secondary);'>Enter patient information to generate a disease-risk prediction.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Go to Patient Prediction", icon=":material/clinical_notes:"):
        st.switch_page("views/patient_prediction.py")
else:
    result_data = st.session_state['last_prediction']
    pred = result_data['result']
    probs = result_data['probabilities']
    classes = result_data['classes']

    colors = {"Low": "#19A974", "Medium": "#F4A62A", "High": "#E85C68"}
    color = colors.get(pred, "var(--primary)")

    st.markdown(
        f"""
        <div class='glass-card' style='padding: 2rem 1.5rem; text-align: center; border-radius: 26px; background: linear-gradient(180deg, rgba(255,255,255,0.84), rgba(245,247,253,0.9));'>
            <div style='display: inline-flex; align-items: center; justify-content: center; width: 96px; height: 96px; border-radius: 28px; background: linear-gradient(135deg, {color}, rgba(16,185,129,0.18)); box-shadow: 0 18px 34px rgba(16,185,129,0.18); margin-bottom: 1rem; color: white; font-size: 2.1rem; font-weight: 800;'>{pred[0].upper()}</div>
            <div style='font-size: 0.75rem; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase; color: {color};'>Disease Risk Level</div>
            <h1 style='margin: 0.5rem 0; color: {color}; font-size: clamp(2.2rem, 4vw, 3.2rem);'>{pred.upper()} RISK</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if probs is not None:
        st.markdown("<div class='section-eyebrow' style='margin-top: 1.4rem;'>Prediction Confidence</div>", unsafe_allow_html=True)
        card_cols = st.columns(3)
        for idx, (cls, prob) in enumerate(zip(classes, probs)):
            with card_cols[idx]:
                bar_color = {"Low": "#19A974", "Medium": "#F4A62A", "High": "#E85C68"}.get(cls, "var(--primary)")
                st.markdown(
                    f"""
                    <div class='glass-card' style='padding: 1rem; border-top: 4px solid {bar_color};'>
                        <div style='font-size: 0.76rem; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; color: {bar_color};'>{cls}</div>
                        <div style='font-size: 1.8rem; font-weight: 800; margin-top: 0.4rem;'>{prob*100:.1f}%</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

render_footer()