# Diabetes ETL + EDA Pipeline

A modular, end-to-end **Data Engineering & Analysis** project built for the *Diabetes Prediction Dataset*.

This repository implements:

- **Part 1: Data Validation & ETL**
- **Part 2: Exploratory Data Analysis (EDA)**

---

## Project Structure

```bash 

diabetes-etl-eda/
│
├── data/
│   └── diabetes.csv                # raw input data
│
├── etl/                            # data engineering modules
│   ├── schema_validation.py
│   ├── cleaning.py
│   ├── encoding_scaling.py
│   └── stratified_split.py
│
├── eda/                            # exploratory analysis modules
│   ├── summary_stats.py
│   ├── correlations.py
│   ├── risk_groups.py
│   ├── visualizations.py
│   └── multicollinearity.py
│
├── main.py                         # orchestrates full pipeline
├── requirements.txt
└── README.md

```


---

## Part 1 — Data Validation & ETL

### Steps Performed
| Step | Description | Output File |
|------|--------------|--------------|
| **1. Schema Validation** | Validates required columns: `gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level, diabetes` | — |
| **2. Cleaning + Quarantine** | Removes invalid / missing / out-of-range data; quarantines bad rows with reasons | `out/clean.csv`, `out/quarantine.csv` |
| **3. Encoding + Z-Score Scaling** | One-hot encodes categorical columns and scales continuous features | `out/encode_scaled.csv` |
| **4. Stratified Train/Valid/Test Split** | Creates class-balanced splits for modeling | `out/splits/train.csv`, `valid.csv`, `test.csv` |

---

## Part 2 — Exploratory Data Analysis

### Steps Performed
| Step | Description | Output |
|------|--------------|--------|
| **1. Summary Statistics** | Mean, std, min, median, max, % missing | `out/summary_stats.csv` |
| **2. Correlations** | Pearson correlation with diabetes target | `out/correlation.json` |
| **3. Risk Group Stats** | Diabetes prevalence by risk group: elderly, overweight, hypertension, heart disease, high glucose, smokers | `out/risk_groups.csv` |
| **4. Visualizations** | Histograms, boxplots, bar charts | `out/plots/` |
| **5. Multicollinearity Check** | Warns if any |r| > 0.8 among numeric predictors | `out/multicollinearity.txt` |

---

## Dataset Notes

**Target:** `diabetes` (0 = No, 1 = Yes)

**Allowed values for `smoking_history`:**


current, ever, former, never, No Info, not current

``` bash

Any other values are quarantined as invalid.

**Smoker definition (for risk groups):**

```

smoking_history ∈ {current, ever, former, not current}

## Run the project

```bash

---

## ⚙️ Running the Project

### Install dependencies
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

```

### Place your dataset

Place your raw CSV inside the data/ folder:
```bash
data/diabetes_prediction_dataset.csv
```

### Run the pipeline

```bash
python main.py
```

### Check outputs

All results are generated inside the out/ folder:

```bash

out/
├── clean.csv
├── clean_scaled.csv
├── quarantine.csv
├── summary_stats.csv
├── correlation.json
├── risk_groups.csv
├── multicollinearity.txt
├── plots/
│   ├── hist_age.png
│   ├── box_bmi.png
│   ├── bar_smoking_diabetes.png
│   └── ...
└── splits/
    ├── train.csv
    ├── valid.csv
    └── test.csv

```

