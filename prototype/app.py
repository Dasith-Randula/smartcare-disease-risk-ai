import streamlit as st
from utils.ui_utils import apply_custom_css, get_icon_svg

st.set_page_config(page_title="SmartCare AI", layout="wide", initial_sidebar_state="expanded")

if 'theme' not in st.session_state:
    st.session_state['theme'] = 'Light'

apply_custom_css()

pages = {
    "Navigation": [
        st.Page("views/home.py", title="Home", icon=":material/home:", default=True),
        st.Page("views/patient_prediction.py", title="Patient Prediction", icon=":material/clinical_notes:"),
        st.Page("views/prediction_result.py", title="Prediction Result", icon=":material/health_and_safety:"),
        st.Page("views/eda_dashboard.py", title="EDA Dashboard", icon=":material/analytics:"),
        st.Page("views/model_performance.py", title="Model Performance", icon=":material/query_stats:"),
        st.Page("views/feature_importance.py", title="Feature Importance", icon=":material/psychology:"),
        st.Page("views/about.py", title="About & Disclaimer", icon=":material/info:")
    ]
}

with st.sidebar:
    st.markdown(
        f"""
        <div class='sidebar-brand'>
            <div class='brand-logo'>{get_icon_svg('hospital', 18, '#ffffff')}</div>
            <div class='brand-title'>SmartCare AI</div>
        </div>
        <div class='brand-subtitle'>Disease Risk Prediction</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<div class='sidebar-card'>AI-powered clinical intelligence for better patient outcomes.</div>", unsafe_allow_html=True)
    st.divider()

    pg = st.navigation(pages)

    st.divider()
    st.markdown("<div style='font-weight:700; margin-bottom: 0.5rem;'>Appearance</div>", unsafe_allow_html=True)
    theme_choice = st.radio("Theme", ["Light", "Dark"], index=0 if st.session_state['theme'] == 'Light' else 1, horizontal=True)
    if theme_choice != st.session_state['theme']:
        st.session_state['theme'] = theme_choice
        st.rerun()

pg.run()