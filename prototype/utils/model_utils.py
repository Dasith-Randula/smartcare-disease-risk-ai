import streamlit as st
import joblib
import pandas as pd
import pathlib
from datetime import datetime

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent.resolve()
MODELS_DIR = PROJECT_ROOT / "models"

@st.cache_resource
def load_model_and_encoder():
    try:
        model = joblib.load(MODELS_DIR / "best_disease_risk_model.joblib")
        encoder = joblib.load(MODELS_DIR / "disease_risk_label_encoder.joblib")
        return model, encoder
    except Exception as e:
        return None, None

def engineer_features(input_data):
    """Applies exact feature engineering from Task 03."""
    df = pd.DataFrame([input_data])
    
    # Date features
    if 'Appointment Date' in df.columns:
        date_obj = pd.to_datetime(df['Appointment Date'][0])
        df['appointment_year'] = date_obj.year
        df['appointment_month'] = date_obj.month
        df['appointment_day'] = date_obj.day
        df['appointment_dayofweek'] = date_obj.dayofweek
        df['appointment_is_weekend'] = 1 if date_obj.dayofweek >= 5 else 0
        df = df.drop(columns=['Appointment Date'])
        
    # Financial features
    df['calculated_total_bill'] = df.get('Consultation Charge', 0) + df.get('Laboratory Charge', 0) + df.get('Room Charge', 0) + df.get('Medicine Charge', 0)
    
    # Clinical features
    df['stay_duration'] = df.get('Length of Stay', 1)
    df['care_intensity_index'] = df.get('Lab Tests Count', 0) + df.get('Treatments Count', 0)
    
    return df

def predict_risk(model, encoder, processed_df):
    prediction = model.predict(processed_df)
    probabilities = model.predict_proba(processed_df)[0] if hasattr(model, 'predict_proba') else None
    
    # Inverse transform to get Low/Medium/High
    predicted_class = encoder.inverse_transform(prediction)[0]
    
    return predicted_class, probabilities, encoder.classes_