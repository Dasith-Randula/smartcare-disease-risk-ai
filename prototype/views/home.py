import streamlit as st
from utils.ui_utils import get_icon_svg, render_footer

hero_left, hero_right = st.columns([1.05, 0.95], gap="large")

with hero_left:
    st.markdown("<div class='section-eyebrow'>AI-POWERED HEALTHCARE INTELLIGENCE</div>", unsafe_allow_html=True)
    st.markdown("<h1>SmartCare AI</h1>", unsafe_allow_html=True)
    st.markdown("<div class='hero-subtitle'>Disease Risk Prediction System</div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class='hero-description'>
            <div class='hero-icon'>{get_icon_svg('shield', 22, 'var(--primary)')}</div>
            <p>A machine-learning clinical decision-support prototype that classifies patient disease risk into Low, Medium, or High categories using SmartCare hospital data.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Predict Patient Risk", type="primary", icon=":material/neurology:"):
        st.switch_page("views/patient_prediction.py")

with hero_right:
    st.markdown(
        f"""
        <div class='hero-scene'>
            <div class='hero-platforms'>
                <div class='hero-platform platform-back'></div>
                <div class='hero-platform'></div>
                <div class='hero-cube-wrap'>
                    <div class='hero-cube'><span>AI</span></div>
                </div>
                <div class='hero-object heart'>{get_icon_svg('monitor_heart', 26, 'var(--primary)')}</div>
                <div class='hero-object cross'>{get_icon_svg('medical_services', 24, 'var(--primary)')}</div>
                <div class='hero-object chart'>{get_icon_svg('bar_chart', 22, 'var(--primary)')}</div>
                <div class='hero-sphere one'></div>
                <div class='hero-sphere two'></div>
                <div class='hero-sphere three'></div>
                <div class='hero-sphere four'></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div class='metric-section-title'>System Metrics</div>", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3, gap="large")
with m1:
    st.markdown(
        f"""
        <div class='metric-card'>
            <div class='metric-icon blue'>{get_icon_svg('users', 28, 'var(--primary)')}</div>
            <div class='metric-value'>1,000</div>
            <div class='metric-label'>Patient Records</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with m2:
    st.markdown(
        f"""
        <div class='metric-card'>
            <div class='metric-icon cyan'>{get_icon_svg('analytics', 28, '#21C1C3')}</div>
            <div class='metric-value'>4</div>
            <div class='metric-label'>Base ML Models</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with m3:
    st.markdown(
        f"""
        <div class='metric-card'>
            <div class='metric-icon purple'>{get_icon_svg('target', 28, '#7048F5')}</div>
            <div class='metric-value'>94.5%</div>
            <div class='metric-label'>Best Accuracy</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

render_footer()