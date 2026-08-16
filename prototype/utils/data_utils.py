import streamlit as st
import pandas as pd
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent.resolve()
DATA_DIR = PROJECT_ROOT / "data" / "raw"
FIGURES_DIR = PROJECT_ROOT / "outputs" / "figures"

@st.cache_data
def load_dataset():
    """Loads the dataset to extract dropdown options."""
    try:
        # Looking for the 1000 row dataset as per prompt
        csv_files = list(DATA_DIR.glob("*1000.csv"))
        if csv_files:
            return pd.read_csv(csv_files[0])
        return pd.DataFrame() # Fallback
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()

def get_figure_path(filename):
    """Returns the absolute path to a requested figure."""
    return FIGURES_DIR / filename