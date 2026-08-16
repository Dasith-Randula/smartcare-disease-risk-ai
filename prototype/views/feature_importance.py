import streamlit as st
from utils.data_utils import get_figure_path
from utils.ui_utils import render_footer
from PIL import Image
import os

st.title("Feature Importance")
st.markdown("""
<div class='surface-card'>
Understand which patient and hospital features influence model predictions the most.
</div>
""", unsafe_allow_html=True)

def show_img(filename):
    path = get_figure_path(filename)
    if os.path.exists(path):
        st.image(Image.open(path), width="stretch")
    else:
        st.warning(f"Figure {filename} not found.")

col1, col2 = st.columns([0.6, 0.4])

with col1:
    show_img("permutation_feature_importance.png")

with col2:
    st.markdown("""
    <div class='glass-card'>
        <h3 class='insight-title'>Insights</h3>
        <p>Permutation importance measures how much model performance decreases when each feature is shuffled.</p>
        <hr>
        <p><i>These values describe global model behaviour and do not establish medical causation.</i></p>
        <br>
        <h4>Key Indicators:</h4>
        <ul>
            <li>Blood Sugar</li>
            <li>Cholesterol</li>
            <li>Age</li>
            <li>BMI</li>
            <li>Previous Admissions</li>
            <li>Systolic Blood Pressure</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

render_footer()