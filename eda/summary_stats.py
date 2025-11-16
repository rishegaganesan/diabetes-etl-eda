import pandas as pd
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