import streamlit as st
from utils.data_utils import load_dataset
from utils.model_utils import load_model_and_encoder, engineer_features, predict_risk
from utils.ui_utils import render_footer

st.title("Patient Disease Risk Prediction")
st.markdown("""
<div class='surface-card'>
Enter patient details to estimate the disease-risk category.
</div>
""", unsafe_allow_html=True)

df = load_dataset()

# Helper function for safe column lookup
def get_options(col_name, default_list):
    if not df.empty and col_name in df.columns:
        return df[col_name].dropna().unique().tolist()
    return default_list

with st.form("prediction_form"):
    tab1, tab2, tab3 = st.tabs(["🩺 Patient & Clinical", "🏥 Hospital", "💳 Financial"])
    
    with tab1:
        col1, col2 = st.columns(2)
        age = col1.number_input("Age", min_value=0, max_value=120, value=45)
        gender = col2.selectbox("Gender", get_options('Gender', ['Male', 'Female']))
        blood_group = col1.selectbox("Blood Group", get_options('Blood Group', ['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-']))
        diagnosis = col2.selectbox("Diagnosis", get_options('Diagnosis', ['General', 'Cardiac', 'Respiratory']))
        sys_bp = col1.number_input("Systolic BP", value=120)
        dia_bp = col2.number_input("Diastolic BP", value=80)
        blood_sugar = col1.number_input("Blood Sugar", value=100)
        cholesterol = col2.number_input("Cholesterol", value=180)
        bmi = col1.number_input("BMI", value=24.5)

    with tab2:
        col3, col4 = st.columns(2)
        department = col3.selectbox("Department", get_options('Department', ['Cardiology', 'General']))
        apt_date = col4.date_input("Appointment Date")
        prev_apt = col3.number_input("Previous Appointments", value=0)
        missed_apt = col4.number_input("Missed Previous Appointments", value=0)
        apt_status = col3.selectbox("Appointment Status", get_options('Appointment Status', ['Completed', 'Pending']))
        prev_admissions = col4.number_input("Previous Admissions", value=0)
        admitted = col3.selectbox("Admitted", get_options('Admitted', ['Yes', 'No']))
        los = col4.number_input("Length of Stay (Days)", value=1)
        room_type = col3.selectbox("Room Type", get_options('Room Type', ['General', 'ICU', 'Private']))
        lab_tests = col4.number_input("Lab Tests Count", value=1)
        treatments = col3.number_input("Treatments Count", value=1)

    with tab3:
        col5, col6 = st.columns(2)
        consult_charge = col5.number_input("Consultation Charge", value=50.0)
        lab_charge = col6.number_input("Laboratory Charge", value=20.0)
        room_charge = col5.number_input("Room Charge", value=100.0)
        med_charge = col6.number_input("Medicine Charge", value=30.0)
        pay_status = col5.selectbox("Payment Status", get_options('Payment Status', ['Paid', 'Pending']))
        pay_method = col6.selectbox("Payment Method", get_options('Payment Method', ['Card', 'Cash', 'Insurance']))

    submitted = st.form_submit_button("🔮 Predict Disease Risk")

if submitted:
    input_data = {
        'Age': age, 'Gender': gender, 'Blood Group': blood_group, 'Diagnosis': diagnosis,
        'Systolic BP': sys_bp, 'Diastolic BP': dia_bp, 'Blood Sugar': blood_sugar,
        'Cholesterol': cholesterol, 'BMI': bmi, 'Department': department,
        'Appointment Date': apt_date, 'Previous Appointments': prev_apt,
        'Missed Previous Appointments': missed_apt, 'Appointment Status': apt_status,
        'Previous Admissions': prev_admissions, 'Admitted': admitted, 'Length of Stay': los,
        'Room Type': room_type, 'Lab Tests Count': lab_tests, 'Treatments Count': treatments,
        'Consultation Charge': consult_charge, 'Laboratory Charge': lab_charge,
        'Room Charge': room_charge, 'Medicine Charge': med_charge,
        'Payment Status': pay_status, 'Payment Method': pay_method
    }
    
    model, encoder = load_model_and_encoder()
    if model is None:
        st.error("Model files not found! Please check repository paths.")
    else:
        processed_df = engineer_features(input_data)
        
        try:
            prediction, probs, classes = predict_risk(model, encoder, processed_df)
            st.session_state['last_prediction'] = {
                'result': prediction,
                'probabilities': probs,
                'classes': classes
            }
            st.switch_page("views/prediction_result.py")
        except Exception as e:
            st.error(f"Prediction error: {e}. Note: Ensure form inputs exactly match notebook features.")

render_footer()