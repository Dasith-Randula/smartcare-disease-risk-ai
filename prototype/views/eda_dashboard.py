import os
import streamlit as st
from PIL import Image
from utils.data_utils import get_figure_path
from utils.ui_utils import render_footer, render_page_header

render_page_header("Exploratory Data Analysis", "Interactive review of the SmartCare clinical dataset and model drivers.", eyebrow="Data Exploration", icon="analytics")

tabs = st.tabs(["Overview", "Distributions", "Relationships", "Categorical", "Heatmap"])


def show_img(filename):
    path = get_figure_path(filename)
    if os.path.exists(path):
        st.markdown("<div class='chart-card' style='padding: 1rem; border-radius: 18px;'>", unsafe_allow_html=True)
        st.image(Image.open(path), width="stretch")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning(f"Figure {filename} not found.")

with tabs[0]:
    col1, col2 = st.columns(2)
    with col1: show_img("target_distribution.png")
    with col2: show_img("age_histogram.png")

with tabs[1]:
    col1, col2 = st.columns(2)
    with col1: show_img("bmi_histogram.png")
    with col2: show_img("blood_sugar_mg_dl_histogram.png")

with tabs[2]:
    show_img("clinical_features_boxplot.png")

with tabs[3]:
    col1, col2 = st.columns(2)
    with col1: show_img("gender_vs_disease_risk_level.png")
    with col2: show_img("department_vs_disease_risk_level.png")

with tabs[4]:
    show_img("correlation_heatmap.png")

render_footer()