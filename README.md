# SmartCare Disease Risk AI

An Explainable Artificial Intelligence system for classifying hospital patients into **Low, Medium, and High disease-risk categories** using demographic, clinical, hospital, and healthcare information.

This project is developed using the **SmartCare Hospital dataset** as part of the CCS3440 Artificial Intelligence module.

---

## Project Overview

Early identification of patient disease risk can support preventive healthcare interventions and improve clinical decision-making.

The objective of this project is to develop and evaluate machine learning models capable of classifying patients into three disease-risk categories:

* Low Risk
* Medium Risk
* High Risk

The project follows a complete machine learning lifecycle including data understanding, preprocessing, exploratory data analysis, feature engineering, model development, model evaluation, Explainable AI, and prototype development.

---

## Problem Type

**Multi-Class Classification**

### Target Variable

`disease_risk_level`

### Target Classes

* `Low`
* `Medium`
* `High`

---

## Dataset

The SmartCare Hospital dataset contains **1,000 hospital records** containing information from several areas of healthcare.

### Patient Information

* Age
* Gender
* Blood Group

### Clinical Information

* Diagnosis
* Systolic Blood Pressure
* Diastolic Blood Pressure
* Blood Sugar
* Cholesterol
* BMI

### Hospital Information

* Department
* Appointment History
* Previous Admissions
* Length of Stay
* Room Type
* Laboratory Tests
* Treatments

### Financial Information

* Consultation Charges
* Laboratory Charges
* Medicine Charges
* Room Charges
* Total Bill

The target used for this project is `disease_risk_level`.

---

## Project Workflow

The project follows the machine learning workflow below:

```text
SmartCare Dataset
        ↓
Dataset Understanding
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Feature Selection
        ↓
Train / Test Split
        ↓
Machine Learning Models
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Best Model Selection
        ↓
Explainable AI
        ↓
Model Deployment
        ↓
Streamlit Clinical Decision-Support Prototype
```

---

## Machine Learning Models

Multiple classification algorithms will be developed and compared.

Planned models include:

* Multinomial Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* Support Vector Machine
* XGBoost Classifier

The final model will be selected based on comparative evaluation rather than accuracy alone.

---

## Model Evaluation

Models will be evaluated using multi-class classification metrics including:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Cross-Validation Performance

Where appropriate, macro and weighted averages will be considered to provide a more complete evaluation of performance across all disease-risk classes.

---

## Explainable AI

Explainable AI techniques will be used to understand why the trained model generates particular predictions.

The project will primarily investigate:

* SHAP
* Feature Importance
* Global feature influence
* Individual patient prediction explanations

Explainability is particularly important in healthcare-related AI systems because predictions should be understandable and transparent.

---

## Prototype

A Streamlit-based prototype will provide an interactive interface for entering patient information and generating disease-risk predictions.

The prototype is intended to display:

* Predicted disease-risk category
* Prediction probabilities
* Important contributing features
* Explainable AI information

Example output:

```text
Predicted Risk Level: HIGH

Prediction Probabilities
Low Risk:       5%
Medium Risk:   17%
High Risk:     78%
```

---

## Technology Stack

### Programming Language

* Python

### Development Environment

* Visual Studio Code
* Jupyter Notebook

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost

### Explainable AI

* SHAP

### Prototype

* Streamlit

### Model Persistence

* Joblib

### Version Control

* Git
* GitHub

---

## Project Structure

```text
smartcare-disease-risk-ai/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│
├── models/
│
├── app/
│
├── reports/
│
├── outputs/
│   ├── figures/
│   └── metrics/
│
├── tests/
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/smartcare-disease-risk-ai.git
```

Move into the project directory:

```bash
cd smartcare-disease-risk-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Jupyter Notebook

Open the project using Visual Studio Code and select the Python virtual environment as the Jupyter kernel.

The main analysis notebook is located at:

```text
notebooks/smartcare_disease_risk_analysis.ipynb
```

---

## Running the Streamlit Application

From the project root directory:

```bash
streamlit run app/app.py
```

---

## Disclaimer

This project is developed for educational and research purposes.

The generated disease-risk classifications must not be interpreted as medical diagnoses or used as a replacement for professional clinical judgement. The system is intended only to demonstrate machine learning and Explainable AI techniques using the provided SmartCare dataset.

---

## Author

**Dasith**

CCS3440 – Artificial Intelligence

---

## Project Status

🚧 Development in progress.
