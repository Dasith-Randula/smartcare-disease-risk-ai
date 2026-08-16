import os
import streamlit as st
from PIL import Image
from utils.data_utils import get_figure_path
from utils.ui_utils import get_icon_svg, render_footer, render_page_header

render_page_header("Model Performance", "Review the best-performing classifier and model metrics.", eyebrow="Model Intelligence", icon="query_stats")


def show_img(filename):
    path = get_figure_path(filename)
    if os.path.exists(path):
        st.markdown("<div class='chart-card' style='padding: 1rem; border-radius: 18px;'>", unsafe_allow_html=True)
        st.image(Image.open(path), width="stretch")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning(f"Figure {filename} not found.")

st.markdown(
    """
    <div class='glass-card' style='padding: 1.15rem 1.3rem; border-left: 5px solid #4F6FF7; border-radius: 20px;'>
        <div style='font-size: 0.72rem; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase; color: #4F6FF7;'>Best Performing Model</div>
        <h3 style='margin: 0.45rem 0 0;'>Logistic Regression</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)
with col1:
    show_img("model_comparison_f1_macro.png")
with col2:
    show_img("best_model_confusion_matrix.png")

m1, m2, m3, m4 = st.columns(4)
m1.markdown(f"<div class='metric-card'><div class='metric-icon blue'>{get_icon_svg('target', 26, '#4169F5')}</div><div class='metric-value'>94.5%</div><div class='metric-label'>Accuracy</div></div>", unsafe_allow_html=True)
m2.markdown(f"<div class='metric-card'><div class='metric-icon cyan'>{get_icon_svg('query_stats', 26, '#21C1C3')}</div><div class='metric-value'>0.9397</div><div class='metric-label'>Macro Precision</div></div>", unsafe_allow_html=True)
m3.markdown(f"<div class='metric-card'><div class='metric-icon purple'>{get_icon_svg('analytics', 26, '#7048F5')}</div><div class='metric-value'>0.9220</div><div class='metric-label'>Macro Recall</div></div>", unsafe_allow_html=True)
m4.markdown(f"<div class='metric-card'><div class='metric-icon blue'>{get_icon_svg('info', 26, '#4169F5')}</div><div class='metric-value'>0.9303</div><div class='metric-label'>Macro F1</div></div>", unsafe_allow_html=True)

render_footer()