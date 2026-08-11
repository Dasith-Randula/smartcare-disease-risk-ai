import json
from pathlib import Path

path = Path(r"c:\Users\User\Desktop\Assignments\SEM 7\AI\Assignment 02\smartcare-disease-risk-ai\notebooks\smartcare_disease_risk_analysis.ipynb")
nb = json.loads(path.read_text(encoding="utf-8"))

# Remove stale outputs from previous runs so we generate fresh output from execution.
for cell in nb["cells"]:
    cell["outputs"] = []
    cell["execution_count"] = None

# Core imports and setup
nb["cells"][3]["source"] = '''import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

plt.style.use("seaborn-v0_8-whitegrid")
pd.set_option("display.max_columns", None)

PROJECT_ROOT = Path("..")
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
FIGURES_DIR = PROJECT_ROOT / "outputs" / "figures"
METRICS_DIR = PROJECT_ROOT / "outputs" / "metrics"
MODELS_DIR = PROJECT_ROOT / "models"

for p in [PROCESSED_DATA_DIR, FIGURES_DIR, METRICS_DIR, MODELS_DIR]:
    p.mkdir(parents=True, exist_ok=True)

data_path = RAW_DATA_DIR / "smartcare_ai_dataset_1000.csv"
dict_path = RAW_DATA_DIR / "smartcare_ai_dataset_data_dictionary.csv"

assert data_path.exists(), f"Raw data file not found: {data_path}"
assert dict_path.exists(), f"Data dictionary file not found: {dict_path}"

df = pd.read_csv(data_path)
df_dict = pd.read_csv(dict_path)

print(f"Dataset Shape: {df.shape}")
display(df.head())
'''.splitlines(keepends=True)

# Data understanding
nb["cells"][5]["source"] = "df.info()\n".splitlines(keepends=True)
nb["cells"][6]["source"] = "display(df_dict)\n".splitlines(keepends=True)
nb["cells"][9]["source"] = '''missing_summary = df.isnull().sum()
missing_summary = missing_summary[missing_summary > 0]
print("Missing values per feature:")
display(missing_summary)

duplicates = df.duplicated().sum()
print(f"Duplicate records: {duplicates}")
'''.splitlines(keepends=True)
nb["cells"][11]["source"] = '''data = df.copy()
data["room_type"] = data["room_type"].fillna("None")
print("Prepared data rows:", data.shape[0])
print(data["room_type"].value_counts(dropna=False).head())
'''.splitlines(keepends=True)

# Feature engineering and target preview
nb["cells"][13]["source"] = '''financial_cols = [
    "consultation_fee_lkr",
    "lab_charge_lkr",
    "room_charge_lkr",
    "medicine_charge_lkr",
]

if all(col in data.columns for col in financial_cols):
    data["calculated_total_bill"] = (
        data["consultation_fee_lkr"].fillna(0)
        + data["lab_charge_lkr"].fillna(0)
        + data["room_charge_lkr"].fillna(0)
        + data["medicine_charge_lkr"].fillna(0)
    )

    if "total_bill_lkr" in data.columns:
        diff_median = (data["calculated_total_bill"] - data["total_bill_lkr"]).abs().median()
        print("Median absolute difference between calculated and reported total bill:", diff_median)
else:
    print("Required financial columns are not available.")

care_cols = [
    "lab_tests_count",
    "treatments_count",
    "length_of_stay_days",
]

if all(col in data.columns for col in care_cols):
    data["stay_duration"] = data["length_of_stay_days"].fillna(1).clip(lower=1)
    data["care_intensity_index"] = (
        data["lab_tests_count"].fillna(0)
        + data["treatments_count"].fillna(0)
    ) / data["stay_duration"]
    print("Care intensity index created.")
else:
    print("Required care intensity columns are not available.")

engineered_cols = [
    col for col in ["calculated_total_bill", "stay_duration", "care_intensity_index"]
    if col in data.columns
]

display(data[engineered_cols].head())
'''.splitlines(keepends=True)
nb["cells"][15]["source"] = '''if "disease_risk_level" in data.columns:
    print("Target value counts:")
    display(data["disease_risk_level"].value_counts())
else:
    print("Target column not found in data")
'''.splitlines(keepends=True)

# EDA visuals
nb["cells"][18]["source"] = '''plt.figure(figsize=(7, 5))
sns.countplot(data=data, x="disease_risk_level", order=None, palette="Blues_d")
plt.title("Distribution of Disease Risk Level")
plt.xlabel("Risk Level")
plt.ylabel("Patient Count")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "target_distribution.png", dpi=300)
plt.show()

vc = data["disease_risk_level"].value_counts()
vp = data["disease_risk_level"].value_counts(normalize=True) * 100
print("Class counts:\n", vc)
print("\nClass percentages (%):\n", vp.round(2))
'''.splitlines(keepends=True)
nb["cells"][19]["source"] = '''num_plot_cols = [
    "age",
    "systolic_bp",
    "diastolic_bp",
    "blood_sugar_mg_dl",
    "cholesterol_mg_dl",
    "bmi",
    "lab_tests_count",
    "treatments_count",
]
cols = [c for c in num_plot_cols if c in data.columns]

for col in cols:
    plt.figure(figsize=(7, 4))
    sns.histplot(data=data, x=col, kde=True, bins=30)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"{col}_histogram.png", dpi=300)
    plt.show()
'''.splitlines(keepends=True)
nb["cells"][21]["source"] = '''fig, axes = plt.subplots(2, 2, figsize=(12, 10))
cols = [
    ("age", "Age vs Disease Risk Level"),
    ("bmi", "BMI vs Disease Risk Level"),
    ("blood_sugar_mg_dl", "Blood Sugar vs Disease Risk Level"),
    ("cholesterol_mg_dl", "Cholesterol vs Disease Risk Level"),
]

for ax, (col, title) in zip(axes.flatten(), cols):
    if col in data.columns:
        sns.boxplot(data=data, x="disease_risk_level", y=col, ax=ax, order=None)
        ax.set_title(title)
    else:
        ax.set_visible(False)

plt.tight_layout()
plt.savefig(FIGURES_DIR / "clinical_features_boxplot.png", dpi=300)
plt.show()
'''.splitlines(keepends=True)
nb["cells"][23]["source"] = '''plt.figure(figsize=(8, 6))
if all(c in data.columns for c in ["blood_sugar_mg_dl", "cholesterol_mg_dl"]):
    sns.scatterplot(
        data=data,
        x="blood_sugar_mg_dl",
        y="cholesterol_mg_dl",
        hue="disease_risk_level",
        palette="Set1",
        alpha=0.8,
    )
    plt.title("Blood Sugar vs Cholesterol by Disease Risk Level")
    plt.xlabel("Blood Sugar (mg/dL)")
    plt.ylabel("Cholesterol (mg/dL)")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "blood_sugar_vs_cholesterol_scatter.png", dpi=300)
    plt.show()
else:
    print("Required columns for scatter plot not present; skipping.")
'''.splitlines(keepends=True)
nb["cells"][25]["source"] = '''numeric_df = data.select_dtypes(include=[np.number]).copy()
exclude_cols = {"disease_risk_encoded"}
for c in list(exclude_cols):
    if c in numeric_df.columns:
        numeric_df = numeric_df.drop(columns=c)

corr = numeric_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=False, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix of Numerical Attributes")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "correlation_heatmap.png", dpi=300)
plt.show()
'''.splitlines(keepends=True)
nb["cells"][26]["source"] = '''cat_candidates = ["gender", "diagnosis", "department", "blood_group", "room_type", "payment_status", "admitted"]
available = [c for c in cat_candidates if c in data.columns]
print("Categorical columns available for simple analysis:", available)

for c in available:
    ct = pd.crosstab(data[c], data["disease_risk_level"], normalize="index") * 100
    display(ct.head(10))
    plt.figure(figsize=(8, 4))
    ct.plot(kind="bar", stacked=True, colormap="tab20", legend=True)
    plt.title(f"{c} vs Disease Risk Level (row % normalized)")
    plt.ylabel("Percentage")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"{c}_vs_disease_risk_level.png", dpi=300)
    plt.show()
'''.splitlines(keepends=True)

# Model prep and evaluation
nb["cells"][30]["source"] = '''TARGET = "disease_risk_level"

if TARGET not in data.columns:
    raise KeyError(f"Target column '{TARGET}' not found in dataset")

missing_target = data[TARGET].isnull().sum()
print(f"Missing target labels: {missing_target}")
if missing_target > 0:
    print(f"Removing {missing_target} rows with missing target labels")
    data = data[data[TARGET].notna()].copy()

dup_count = data.duplicated().sum()
print(f"Duplicate rows in dataset: {dup_count}")
if dup_count > 0:
    data = data.drop_duplicates().copy()
    print(f"Duplicates removed. New row count: {data.shape[0]}")

if "appointment_date" in data.columns:
    data["appointment_date"] = pd.to_datetime(data["appointment_date"], errors="coerce")
    data["appointment_year"] = data["appointment_date"].dt.year
    data["appointment_month"] = data["appointment_date"].dt.month
    data["appointment_day"] = data["appointment_date"].dt.day
    data["appointment_dayofweek"] = data["appointment_date"].dt.dayofweek
    data["appointment_is_weekend"] = data["appointment_dayofweek"].isin([5, 6]).astype(int)
    print("Appointment date features created")

identifier_cols = [c for c in ["record_id", "patient_id"] if c in data.columns]
if identifier_cols:
    print("Identifier columns to remove from modelling:", identifier_cols)

leakage_cols = [c for c in ["no_show", "readmitted_30_days"] if c in data.columns]
if leakage_cols:
    print("Columns excluded from predictors due to potential leakage:", leakage_cols)

numeric_cols_all = data.select_dtypes(include=[np.number]).columns.tolist()
exclude_for_outliers = set(identifier_cols + ["disease_risk_encoded"])
numeric_cols = [c for c in numeric_cols_all if c not in exclude_for_outliers]

outlier_summary = []
for col in numeric_cols:
    try:
        col_series = data[col].dropna()
        q1 = col_series.quantile(0.25)
        q3 = col_series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outlier_count = ((col_series < lower) | (col_series > upper)).sum()
        outlier_summary.append({
            "feature": col,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "lower_bound": lower,
            "upper_bound": upper,
            "outlier_count": int(outlier_count),
        })
    except Exception:
        continue

outlier_df = pd.DataFrame(outlier_summary).sort_values(by="outlier_count", ascending=False)
print("Outlier summary (top rows):")
display(outlier_df.head(10))

model_drop_cols = [TARGET] + identifier_cols + leakage_cols
if "appointment_date" in data.columns:
    model_drop_cols.append("appointment_date")

X = data.drop(columns=[col for col in model_drop_cols if col in data.columns])
y = data[TARGET].copy()

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
print("Label encoder classes:", list(label_encoder.classes_))

joblib.dump(label_encoder, MODELS_DIR / "disease_risk_label_encoder.joblib")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded,
)

print(f"Train Size: {X_train.shape[0]} | Test Size: {X_test.shape[0]}")

numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
categorical_features = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

try:
    ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
except TypeError:
    ohe = OneHotEncoder(handle_unknown="ignore", sparse=False)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", ohe),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ],
    remainder="drop",
)

print("Numerical features:", len(numeric_features))
print("Categorical features:", len(categorical_features))
print("Preprocessor created successfully.")
'''.splitlines(keepends=True)
nb["cells"][31]["source"] = '''model_data = X.copy()
model_data[TARGET] = y.values
processed_save_path = PROCESSED_DATA_DIR / "smartcare_disease_risk_model_data.csv"
model_data.to_csv(processed_save_path, index=False)
print("Saved processed model-ready data to", processed_save_path)
'''.splitlines(keepends=True)
nb["cells"][33]["source"] = '''models = {
    "Logistic Regression": LogisticRegression(max_iter=3000, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1),
    "Support Vector Machine": SVC(probability=True, random_state=42),
}

trained_pipelines = {}
cv_results = {}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for name, clf in models.items():
    pipe = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", clf)])
    scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="f1_macro", n_jobs=-1)
    trained_pipelines[name] = pipe.fit(X_train, y_train)
    cv_results[name] = {
        "cv_f1_macro_mean": scores.mean(),
        "cv_f1_macro_std": scores.std(),
    }
    print(f"{name} - CV F1 Macro: {scores.mean():.4f} (+/- {scores.std():.4f})")

rf_param_grid = {
    "classifier__n_estimators": [200, 300],
    "classifier__max_depth": [None, 10, 20],
    "classifier__min_samples_split": [2, 5],
    "classifier__min_samples_leaf": [1, 2],
}
rf_pipe = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", RandomForestClassifier(random_state=42, n_jobs=-1))])
rf_grid = GridSearchCV(rf_pipe, rf_param_grid, cv=cv, scoring="f1_macro", n_jobs=-1, verbose=0)
print("Starting GridSearchCV for Random Forest (this may take a while)...")
rf_grid.fit(X_train, y_train)
print("Random Forest best params:", rf_grid.best_params_)
print("Random Forest best CV F1 Macro:", rf_grid.best_score_)

trained_pipelines["Random Forest (Tuned)"] = rf_grid.best_estimator_
cv_results["Random Forest (Tuned)"] = {
    "cv_f1_macro_mean": rf_grid.best_score_,
    "cv_f1_macro_std": None,
}
'''.splitlines(keepends=True)
nb["cells"][36]["source"] = '''results = {}
for name, pipe in trained_pipelines.items():
    y_pred = pipe.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec_macro = precision_score(y_test, y_pred, average="macro", zero_division=0)
    rec_macro = recall_score(y_test, y_pred, average="macro", zero_division=0)
    f1_macro = f1_score(y_test, y_pred, average="macro", zero_division=0)

    prec_w = precision_score(y_test, y_pred, average="weighted", zero_division=0)
    rec_w = recall_score(y_test, y_pred, average="weighted", zero_division=0)
    f1_w = f1_score(y_test, y_pred, average="weighted", zero_division=0)

    results[name] = {
        "Accuracy": acc,
        "Precision_Macro": prec_macro,
        "Recall_Macro": rec_macro,
        "F1_Macro": f1_macro,
        "Precision_Weighted": prec_w,
        "Recall_Weighted": rec_w,
        "F1_Weighted": f1_w,
    }

results_df = pd.DataFrame(results).T
results_df["CV_F1_Macro_Mean"] = results_df.index.map(lambda n: cv_results.get(n, {}).get("cv_f1_macro_mean"))
results_df["CV_F1_Macro_Std"] = results_df.index.map(lambda n: cv_results.get(n, {}).get("cv_f1_macro_std"))
results_df = results_df.sort_values(by="F1_Macro", ascending=False)

results_df.to_csv(METRICS_DIR / "model_comparison.csv")
print("Saved model comparison to", METRICS_DIR / "model_comparison.csv")

plt.figure(figsize=(8, 4))
sns.barplot(x=results_df.index, y="F1_Macro", data=results_df.reset_index(), palette="magma")
plt.title("Model Comparison (F1 Macro)")
plt.ylabel("F1 Macro")
plt.xlabel("Model")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "model_comparison_f1_macro.png", dpi=300)
plt.show()

display(results_df)
'''.splitlines(keepends=True)
nb["cells"][38]["source"] = '''best_model_name = results_df["F1_Macro"].idxmax()
best_pipeline = trained_pipelines[best_model_name]
print(f"Best Performing Model: {best_model_name}\n")

y_pred_best = best_pipeline.predict(X_test)
class_labels = list(label_encoder.classes_)
print("Detailed Classification Report:")
print(classification_report(y_test, y_pred_best, target_names=class_labels, zero_division=0))

joblib.dump(best_pipeline, MODELS_DIR / "best_disease_risk_model.joblib")
print(f"Model successfully serialized to {MODELS_DIR / 'best_disease_risk_model.joblib'}")

cm = confusion_matrix(y_test, y_pred_best)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=class_labels, yticklabels=class_labels)
plt.title(f"Confusion Matrix - {best_model_name}")
plt.ylabel("Actual Category")
plt.xlabel("Predicted Category")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "best_model_confusion_matrix.png", dpi=300)
plt.show()
'''.splitlines(keepends=True)
nb["cells"][41]["source"] = '''print("Computing permutation importance on the test set...")
perm_res = permutation_importance(
    best_pipeline,
    X_test,
    y_test,
    scoring="f1_macro",
    n_repeats=20,
    random_state=42,
    n_jobs=-1,
)

perm_df = pd.DataFrame({
    "feature": X_test.columns,
    "importance_mean": perm_res.importances_mean,
    "importance_std": perm_res.importances_std,
}).sort_values(by="importance_mean", ascending=False)

perm_df.to_csv(METRICS_DIR / "feature_importance.csv", index=False)
print("Saved permutation importance to", METRICS_DIR / "feature_importance.csv")

top_n = 15
plt.figure(figsize=(8, min(0.4 * top_n + 2, 12)))
sns.barplot(x="importance_mean", y="feature", data=perm_df.head(top_n), palette="viridis")
plt.title(f"Permutation Feature Importance (Top {top_n})")
plt.xlabel("Importance (mean decrease in F1 Macro)")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "permutation_feature_importance.png", dpi=300)
plt.show()

clf = best_pipeline.named_steps["classifier"]
pre = best_pipeline.named_steps["preprocessor"]
if hasattr(clf, "feature_importances_"):
    try:
        transformed_names = pre.get_feature_names_out()
        tree_importances = pd.Series(clf.feature_importances_, index=transformed_names).sort_values(ascending=False)
        plt.figure(figsize=(8, min(0.4 * 15 + 2, 12)))
        tree_importances.head(15).plot(kind="barh", color="teal")
        plt.title("Model Built-in Feature Importances (Top 15)")
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig(FIGURES_DIR / "tree_feature_importance.png", dpi=300)
        plt.show()
    except Exception as e:
        print("Could not compute tree feature importances:", e)
else:
    print("Best model does not expose feature_importances_; skipping tree importances.")
'''.splitlines(keepends=True)

# Replace markdown cells with final academic text
md = {
    0: '''# SmartCare Hospital AI - Disease Risk Classification (Option C)
**Coursework Code:** CCS3440 – Artificial Intelligence  
**Target Variable:** `disease_risk_level` (Multi-Class Classification: Low, Medium, High)  

This notebook covers Tasks 02 to 07 for the selected prediction problem. The target is explicitly the disease risk level, and the remaining patient variables are treated as input features after excluding identifiers and known leakage variables.

---
''',
    1: '''## Task 02: Dataset Understanding

This stage checks the dataset structure, the prediction target, relevant attribute groups, and data quality issues before the model workflow begins.
''',
    2: '''### 2.1 Load Dataset and Libraries

The dataset and the supporting data dictionary are loaded first so the attribute meanings can be checked before any modelling step.
''',
    4: '''### 2.2 Inspect Data Types & Quality Assessment

The dataset contains 1,000 patient records from several healthcare groups. The target variable is `disease_risk_level`, and the other columns are analysed as candidate predictors after excluding unsuitable variables.
''',
    7: '''## Task 03: Data Preprocessing & Feature Engineering

The main preparation steps here are missing-value handling, duplicate checking, outlier review, engineered feature creation, and safe splitting before model training.
''',
    8: '''### 3.1 Check Missing Values & Duplicate Records

The missing-value analysis shows that `room_type` is the main incomplete field, while the duplicate count is zero. This means the data is largely clean, but the room assignment field needs a meaningful handling strategy because it is part of the data dictionary and not just a random missing value.
''',
    10: '''### 3.2 Handling Outliers and Missing Value Imputation

A new copy of the dataset is kept for preprocessing. Missing room assignments are converted to `None`, which matches the dataset dictionary, while numeric missing values are handled later in the sklearn pipeline to avoid leakage from the full dataset.
''',
    12: '''### 3.3 Feature Engineering

The engineered features are created from the existing hospital cost and treatment variables. They summarise payment burden and care intensity in a way that is consistent with the original dataset and does not invent new clinical information.
''',
    14: '''### 3.4 Target Encoding & Export Processed Data

The target distribution is inspected before modelling. The target is not encoded manually during exploration because the label encoder is handled safely within the model pipeline and training split.
''',
    16: '''## Task 04: Exploratory Data Analysis (EDA)

This section reviews the class balance, the spread of important clinical variables, and the relationships between patient features and the risk levels.
''',
    17: '''### 4.1 Target Variable Distribution

The target is not perfectly balanced. Medium-risk patients form the largest group, followed by High-risk and then Low-risk patients. This imbalance matters, so macro metrics are used alongside accuracy when selecting the best model.
''',
    20: '''### 4.2 Numerical Feature Distributions across Risk Levels

The boxplots show that the risk groups differ in their clinical ranges, especially for age, blood sugar, cholesterol, and BMI. The groups overlap somewhat, which indicates that disease risk is a real multi-class problem rather than a simple threshold rule.
''',
    22: '''### 4.3 Scatter Plots & Additional Pattern Visualizations

The blood sugar versus cholesterol scatterplot shows a broad spread across the three risk levels, with higher-risk patients tending to appear in regions with more elevated clinical values. This supports using multiple features together instead of relying on one single measure.
''',
    24: '''### 4.4 Correlation Heatmap

The heatmap shows that the numerical features are not all strongly correlated. This is useful because it suggests that multiple clinically relevant variables contribute to the model rather than one dominant redundant variable.
''',
    27: '''### EDA Interpretation

The dataset is moderately imbalanced, with Medium risk as the most common category and Low risk as the least common. The numerical plots suggest that age, blood pressure, blood sugar, cholesterol, and BMI differ across the risk groups, while the scatterplot indicates that high clinical measurements often align with higher disease risk. Extreme values are kept unless there is clear evidence they are erroneous, because clinically plausible outliers can still reflect real patient conditions.
''',
    28: '''## Task 05: Machine Learning Model Development

The train-test split is performed before preprocessing to avoid leakage. A preprocessing pipeline is then applied to numeric and categorical variables so the selected models are trained on properly prepared features.
''',
    29: '''### 5.1 Train-Test Split & Preprocessing Pipeline Setup

The dataset is split stratified by the target label and a column transformer is used to impute missing values, scale numeric features, and one-hot encode categorical values. This keeps the modelling workflow simple, reproducible, and suitable for undergraduate explanation.
''',
    32: '''### 5.2 Model Training & Hyperparameter Optimization

Four models are trained and compared: Logistic Regression, Decision Tree, Random Forest, and Support Vector Machine. The Random Forest is tuned using only the training data, with 5-fold stratified cross-validation and macro F1 as the tuning score.
''',
    34: '''## Task 06: Model Evaluation

The models are evaluated on the held-out test set using accuracy, macro precision, macro recall, macro F1, and a confusion matrix. Macro F1 is important because the classes are not perfectly balanced and a model that performs well only on the majority class is not necessarily the best classifier.
''',
    35: '''### 6.1 Performance Evaluation Metrics & Comparison Table

The model comparison table shows each model’s performance on the test set. The best model is selected using the highest macro F1 rather than by accuracy alone, because macro F1 better reflects performance across all three disease-risk classes.
''',
    37: '''### 6.2 Best Model Selection, Detailed Classification Report & Confusion Matrix

The selected model is the one with the strongest macro F1 on the test set. The detailed classification report and confusion matrix help explain which classes are easier or harder for the model to identify.
''',
    39: '''## Task 07: Explainable AI (XAI) Analysis

Permutation feature importance is used as the explainable AI method for the selected best model. It measures how much the model’s macro F1 changes when each feature is randomly shuffled, which makes the variable importance easy to interpret.
''',
    40: '''### 7.1 Permutation Feature Importance Analysis

The permutation importance plot shows which features most strongly affect the disease-risk predictions. This approach provides a transparent, model-agnostic explanation while keeping the notebook readable and practical for coursework presentation.
''',
    42: '''### Ethical Implications

The model should be treated as a decision-support tool rather than a replacement for a healthcare professional. Patient privacy, possible bias, class imbalance, and incorrect predictions must be considered when interpreting the results. Human supervision remains necessary, and the predictions should be used to support clinical review rather than to make independent medical decisions.
''',
}
for idx, text in md.items():
    nb["cells"][idx]["source"] = text.splitlines(keepends=True)

# Remove any leftover comments or SHAP references from code cells.
for cell in nb["cells"]:
    if cell.get("cell_type") == "code":
        source = "".join(cell.get("source", []))
        source = source.replace("import shap", "")
        source = source.replace("shap.", "")
        source = source.replace("# ", "")
        source = source.replace("#", "")
        cell["source"] = source.splitlines(keepends=True)

path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Notebook rewritten: {path}")
