import pandas as pd
import os
NUMERIC_COLS = ["age","bmi","HbA1c_level","blood_glucose_level"]

def summary_stats(df: pd.DataFrame, out_path: str):
    summary = []
    for col in NUMERIC_COLS:
        s = df[col]
        summary.append({
            "Feature": col,
            "Mean": s.mean(),
            "Std": s.std(),
            "Min": s.min(),
            "Median": s.median(),
            "Max": s.max(),
            "% Missing": s.isna().mean()*100
        })
    pd.DataFrame(summary).to_csv(out_path, index=False)


    gender_counts = df["gender"].value_counts().rename_axis("Gender").reset_index(name="Count")
    gender_counts.to_csv(os.path.join(os.path.dirname(out_path), "gender_counts.csv"), index=False)

    smoking_counts = df["smoking_history"].value_counts().rename_axis("Smoking History").reset_index(name="Count")
    smoking_counts.to_csv(os.path.join(os.path.dirname(out_path), "smoking_counts.csv"), index=False)

    prevalence = pd.DataFrame({
        "Metric": ["Diabetes Prevalence (%)"],
        "Value": [df["diabetes"].mean() * 100]
    })
    prevalence.to_csv(os.path.join(os.path.dirname(out_path), "diabetes_prevalence.csv"), index=False)
