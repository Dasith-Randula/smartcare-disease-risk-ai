import streamlit as st
from utils.ui_utils import apply_custom_css

# App Configuration must be the first Streamlit command
st.set_page_config(page_title="SmartCare AI", layout="wide", initial_sidebar_state="expanded")

# Initialize theme state
if 'theme' not in st.session_state:
    st.session_state['theme'] = 'Light'

apply_custom_css()

# Define Pages
pages = {
    "Navigation": [
        st.Page("views/home.py", title="Home", icon="🏠", default=True),
        st.Page("views/patient_prediction.py", title="Patient Prediction", icon="🩺"),
        st.Page("views/prediction_result.py", title="Prediction Result", icon="📊"),
        st.Page("views/eda_dashboard.py", title="EDA Dashboard", icon="📈"),
        st.Page("views/model_performance.py", title="Model Performance", icon="⚙️"),
        st.Page("views/feature_importance.py", title="Feature Importance", icon="🔑"),
        st.Page("views/about.py", title="About & Disclaimer", icon="ℹ️")
    ]
}

with st.sidebar:
    st.markdown(
        """
        <div class='sidebar-brand'>
            <div class='brand-logo'>🏥</div>
            <div class='brand-title'>SmartCare AI</div>
        </div>
        <div class='brand-subtitle'>Disease Risk Prediction</div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    pg = st.navigation(pages)

    st.divider()
    st.markdown("### Appearance")
    theme_choice = st.radio("Theme", ["Light", "Dark"], index=0 if st.session_state['theme'] == 'Light' else 1)
    if theme_choice != st.session_state['theme']:
        st.session_state['theme'] = theme_choice
        st.rerun()

pg.run()