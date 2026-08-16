import streamlit as st
from utils.data_utils import load_dataset
from utils.model_utils import (
    engineer_features,
    get_expected_model_columns,
    load_model_and_encoder,
    predict_risk,
    validate_prepared_dataframe,
)
from utils.ui_utils import render_footer, render_page_header

st.markdown("<div class='section-eyebrow'>Clinical Input</div>", unsafe_allow_html=True)
render_page_header("Patient Disease Risk Prediction", "Enter patient details to estimate the disease-risk category.", icon="stethoscope")

raw_df = load_dataset()


def get_options(column_name, fallback_values):
    if not raw_df.empty and column_name in raw_df.columns:
        values = []
        for value in raw_df[column_name].dropna().unique().tolist():
            if value is not None and str(value).strip() != "":
                values.append(value)
        if values:
            return values
    return fallback_values


with st.form("prediction_form"):
    tab1, tab2, tab3 = st.tabs(["Patient & Clinical", "Hospital", "Financial"])

    with tab1:
        col1, col2 = st.columns(2)
        age = col1.number_input("Age", min_value=0, max_value=120, value=45)
        gender = col2.selectbox("Gender", options=get_options("gender", ["Male", "Female"]))
        blood_group = col1.selectbox("Blood Group", options=get_options("blood_group", ["A+", "O+", "B+", "AB+", "A-", "O-", "B-", "AB-"]))
        diagnosis = col2.selectbox("Diagnosis", options=get_options("diagnosis", ["Asthma", "Diabetes", "Hypertension"]))
        systolic_bp = col1.number_input("Systolic BP", value=120)
        diastolic_bp = col2.number_input("Diastolic BP", value=80)
        blood_sugar_mg_dl = col1.number_input("Blood Sugar", value=100)
        cholesterol_mg_dl = col2.number_input("Cholesterol", value=180)
        bmi = col1.number_input("BMI", value=24.5)

    with tab2:
        col3, col4 = st.columns(2)
        department = col3.selectbox("Department", options=get_options("department", ["General Medicine", "Cardiology", "Neurology"]))
        appointment_date = col4.date_input("Appointment Date")
        previous_appointments = col3.number_input("Previous Appointments", min_value=0, value=0)
        missed_previous_appointments = col4.number_input("Missed Previous Appointments", min_value=0, value=0)
        appointment_status = col3.selectbox("Appointment Status", options=get_options("appointment_status", ["Completed", "Scheduled", "No-Show", "Cancelled"]))
        waiting_days = col4.number_input("Waiting Days", min_value=0, value=0)
        previous_admissions = col3.number_input("Previous Admissions", min_value=0, value=0)
        admitted = col4.selectbox(
            "Admitted",
            options=[0, 1],
            format_func=lambda value: "Yes" if value == 1 else "No",
        )
        length_of_stay_days = col3.number_input("Length of Stay (Days)", min_value=1, value=1)
        room_type = col4.selectbox("Room Type", options=get_options("room_type", ["General Ward", "ICU", "Private Room"]))
        lab_tests_count = col3.number_input("Lab Tests Count", min_value=0, value=1)
        treatments_count = col4.number_input("Treatments Count", min_value=0, value=1)

    with tab3:
        col5, col6 = st.columns(2)
        consultation_fee_lkr = col5.number_input("Consultation Charge", min_value=0.0, value=50.0)
        lab_charge_lkr = col6.number_input("Laboratory Charge", min_value=0.0, value=20.0)
        room_charge_lkr = col5.number_input("Room Charge", min_value=0.0, value=100.0)
        medicine_charge_lkr = col6.number_input("Medicine Charge", min_value=0.0, value=30.0)
        total_bill_lkr = col5.number_input("Total Bill Amount", min_value=0.0, value=200.0)
        payment_status = col6.selectbox("Payment Status", options=get_options("payment_status", ["Paid", "Partially Paid", "Unpaid"]))
        payment_method = col5.selectbox("Payment Method", options=get_options("payment_method", ["Card", "Cash", "Insurance", "Online"]))

    submitted = st.form_submit_button("Predict Disease Risk", type="primary", icon=":material/neurology:")

if submitted:
    model, encoder = load_model_and_encoder()
    if model is None:
        st.error("Model files not found. Please check repository paths.")
    else:
        patient_data = {
            "age": age,
            "gender": gender,
            "blood_group": blood_group,
            "department": department,
            "diagnosis": diagnosis,
            "waiting_days": waiting_days,
            "previous_appointments": previous_appointments,
            "missed_previous_appointments": missed_previous_appointments,
            "appointment_status": appointment_status,
            "admitted": admitted,
            "room_type": room_type,
            "length_of_stay_days": length_of_stay_days,
            "previous_admissions": previous_admissions,
            "systolic_bp": systolic_bp,
            "diastolic_bp": diastolic_bp,
            "blood_sugar_mg_dl": blood_sugar_mg_dl,
            "cholesterol_mg_dl": cholesterol_mg_dl,
            "bmi": bmi,
            "lab_tests_count": lab_tests_count,
            "treatments_count": treatments_count,
            "consultation_fee_lkr": consultation_fee_lkr,
            "room_charge_lkr": room_charge_lkr,
            "lab_charge_lkr": lab_charge_lkr,
            "medicine_charge_lkr": medicine_charge_lkr,
            "total_bill_lkr": total_bill_lkr,
            "payment_status": payment_status,
            "payment_method": payment_method,
            "appointment_date": appointment_date,
        }

        try:
            prepared_df = engineer_features(patient_data)
            expected_columns = get_expected_model_columns(model)
            prepared_df = validate_prepared_dataframe(prepared_df, model=model, expected_columns=expected_columns)

            prediction, probabilities, classes = predict_risk(model, encoder, prepared_df)
            st.session_state["last_prediction"] = {
                "result": prediction,
                "probabilities": probabilities,
                "classes": classes,
            }
            st.switch_page("views/prediction_result.py")
        except Exception as exc:
            st.error(f"Prediction error: {exc}")

render_footer()