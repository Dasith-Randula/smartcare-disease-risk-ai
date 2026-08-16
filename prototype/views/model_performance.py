import streamlit as st
from utils.data_utils import get_figure_path
from utils.ui_utils import render_footer
from PIL import Image
import os

st.title("Model Performance")

def show_img(filename):
    path = get_figure_path(filename)
    if os.path.exists(path):
        # Using width='stretch' to avoid the Streamlit deprecation warning
        st.image(Image.open(path), width="stretch")
    else:
        st.warning(f"Figure {filename} not found.")

# Top: Best model card
st.markdown("""
<div class='glass-card'>
    <h4 style='margin:0; color: #4d665b;'>Best Model: Logistic Regression</h4>
</div>
""", unsafe_allow_html=True)

# Middle: Plots
col1, col2 = st.columns(2)
with col1:
    show_img("model_comparison_f1_macro.png")
with col2:
    show_img("best_model_confusion_matrix.png")

# Bottom: Metric cards
m1, m2, m3, m4 = st.columns(4)
m1.markdown("<div class='glass-card'><h4>Accuracy</h4><h2>94.5%</h2></div>", unsafe_allow_html=True)
m2.markdown("<div class='glass-card'><h4>Macro Precision</h4><h2>0.9397</h2></div>", unsafe_allow_html=True)
m3.markdown("<div class='glass-card'><h4>Macro Recall</h4><h2>0.9220</h2></div>", unsafe_allow_html=True)
m4.markdown("<div class='glass-card'><h4>Macro F1</h4><h2>0.9303</h2></div>", unsafe_allow_html=True)

render_footer()