import streamlit as st
from utils.ui_utils import render_footer

st.title("Prediction Result")

if 'last_prediction' not in st.session_state:
    st.info("No prediction is available yet. Enter patient information to generate a disease-risk prediction.")
    if st.button("Go to Patient Prediction", icon=":material/clinical_notes:"):
        st.switch_page("views/patient_prediction.py")
else:
    result_data = st.session_state['last_prediction']
    pred = result_data['result']
    probs = result_data['probabilities']
    classes = result_data['classes']

    colors = {"Low": "#18A97B", "Medium": "#F5A623", "High": "#E85D68"}
    color = colors.get(pred, "#6C5CE7")

    st.markdown(f"""
    <div class='glass-card' style='text-align: center; border-top: 5px solid {color};'>
        <h3>Disease Risk Level</h3>
        <h1 style='color: {color};'>{pred.upper()} RISK</h1>
    </div>
    """, unsafe_allow_html=True)

    if probs is not None:
        st.subheader("Prediction Confidence")
        for cls, prob in zip(classes, probs):
            st.progress(float(prob), text=f"{cls}: {prob*100:.1f}%")

render_footer()