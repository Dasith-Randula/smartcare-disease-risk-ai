import os
import streamlit as st
from PIL import Image
from utils.data_utils import get_figure_path
from utils.ui_utils import render_footer, render_page_header

render_page_header("Feature Importance", "Review the model drivers behind each predicted disease-risk category.", eyebrow="Explainable AI", icon="psychology")


def show_img(filename):
    path = get_figure_path(filename)
    if os.path.exists(path):
        st.markdown("<div class='chart-card' style='padding: 1rem; border-radius: 18px;'>", unsafe_allow_html=True)
        st.image(Image.open(path), width="stretch")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning(f"Figure {filename} not found.")

col1, col2 = st.columns([0.62, 0.38])

with col1:
    show_img("permutation_feature_importance.png")

with col2:
    st.markdown(
        """
        <div class='glass-card' style='padding: 1.25rem 1.15rem; background: linear-gradient(135deg, rgba(114,87,246,0.08), rgba(79,111,247,0.04)); border-left: 5px solid #7257F6; border-radius: 20px;'>
            <div style='font-size: 0.72rem; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase; color: #7257F6;'>Insights</div>
            <p style='margin-top: 0.8rem;'>Permutation importance measures how much model performance decreases when each feature is shuffled.</p>
            <hr style='border: none; border-top: 1px solid rgba(114,87,246,0.18); margin: 0.9rem 0;'> 
            <p><i>These values describe global model behaviour and do not establish medical causation.</i></p>
            <h4 style='margin-top: 0.8rem;'>Key Indicators:</h4>
            <ul>
                <li>Blood Sugar</li>
                <li>Cholesterol</li>
                <li>Age</li>
                <li>BMI</li>
                <li>Previous Admissions</li>
                <li>Systolic Blood Pressure</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

render_footer()