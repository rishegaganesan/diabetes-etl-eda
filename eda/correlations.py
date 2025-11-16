import pandas as pd, json

NUMERIC_COLS = ["age","bmi","HbA1c_level","blood_glucose_level"]
TARGET = "diabetes"

def correlation_analysis(df: pd.DataFrame, out_path: str):
    corr = df[NUMERIC_COLS+[TARGET]].corr(method="pearson")[TARGET].drop(TARGET)
    corr = corr.sort_values(ascending=False)
    with open(out_path, "w") as f:
        json.dump({k: float(v) for k,v in corr.items()}, f, indent=2)