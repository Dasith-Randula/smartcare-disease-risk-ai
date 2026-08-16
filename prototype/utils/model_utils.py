import streamlit as st
import joblib
import pandas as pd
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent.resolve()
MODELS_DIR = PROJECT_ROOT / "models"


@st.cache_resource
def load_model_and_encoder():
    try:
        model = joblib.load(MODELS_DIR / "best_disease_risk_model.joblib")
        encoder = joblib.load(MODELS_DIR / "disease_risk_label_encoder.joblib")
        return model, encoder
    except Exception:
        return None, None


def get_expected_model_columns(model=None):
    """Return the exact feature columns expected by the saved model pipeline."""
    if model is None:
        model, _ = load_model_and_encoder()

    if model is None:
        raise ValueError("Saved model could not be loaded from models/.")

    if hasattr(model, "feature_names_in_"):
        return list(model.feature_names_in_)

    preprocessor = getattr(model, "named_steps", {}).get("preprocessor")
    if preprocessor is not None and hasattr(preprocessor, "feature_names_in_"):
        return list(preprocessor.feature_names_in_)

    raise ValueError("Unable to determine the saved model's expected feature columns.")


def validate_prepared_dataframe(prepared_df, model=None, expected_columns=None):
    """Validate the engineered DataFrame against the saved model schema."""
    if expected_columns is None:
        expected_columns = get_expected_model_columns(model)

    missing = [col for col in expected_columns if col not in prepared_df.columns]
    extra = [col for col in prepared_df.columns if col not in expected_columns]

    if missing or extra:
        raise ValueError(
            "Prepared DataFrame does not match trained model schema. "
            f"Missing: {missing}. Extra: {extra}. "
            f"Expected columns: {len(expected_columns)}."
        )

    return prepared_df.reindex(columns=expected_columns)


def engineer_features(input_data):
    """Apply the same feature engineering used in Task 03 before prediction."""
    df = pd.DataFrame([input_data])

    for col in [
        "age",
        "waiting_days",
        "previous_appointments",
        "missed_previous_appointments",
        "length_of_stay_days",
        "previous_admissions",
        "systolic_bp",
        "diastolic_bp",
        "blood_sugar_mg_dl",
        "cholesterol_mg_dl",
        "bmi",
        "lab_tests_count",
        "treatments_count",
        "consultation_fee_lkr",
        "room_charge_lkr",
        "lab_charge_lkr",
        "medicine_charge_lkr",
        "total_bill_lkr",
        "admitted",
    ]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "appointment_date" in df.columns:
        date_series = pd.to_datetime(df["appointment_date"], errors="coerce")
        df["appointment_year"] = date_series.dt.year
        df["appointment_month"] = date_series.dt.month
        df["appointment_day"] = date_series.dt.day
        df["appointment_dayofweek"] = date_series.dt.dayofweek
        df["appointment_is_weekend"] = date_series.dt.dayofweek.isin([5, 6]).astype(int)
        df = df.drop(columns=["appointment_date"])

    bill_cols = [
        "consultation_fee_lkr",
        "lab_charge_lkr",
        "room_charge_lkr",
        "medicine_charge_lkr",
    ]
    for col in bill_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df["calculated_total_bill"] = df[bill_cols].sum(axis=1)
    df["stay_duration"] = pd.to_numeric(df.get("length_of_stay_days", 1), errors="coerce").fillna(1).clip(lower=1)
    df["care_intensity_index"] = (
        pd.to_numeric(df.get("lab_tests_count", 0), errors="coerce").fillna(0)
        + pd.to_numeric(df.get("treatments_count", 0), errors="coerce").fillna(0)
    ) / df["stay_duration"]

    if "admitted" in df.columns:
        df["admitted"] = pd.to_numeric(df["admitted"], errors="coerce").fillna(0).astype(int)

    if "total_bill_lkr" in df.columns:
        df["total_bill_lkr"] = pd.to_numeric(df["total_bill_lkr"], errors="coerce").fillna(0)

    return df


def predict_risk(model, encoder, processed_df):
    prediction = model.predict(processed_df)
    probabilities = model.predict_proba(processed_df)[0] if hasattr(model, "predict_proba") else None

    predicted_class = encoder.inverse_transform(prediction)[0]
    return predicted_class, probabilities, encoder.classes_