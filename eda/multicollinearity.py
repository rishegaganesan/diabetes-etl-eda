import pandas as pd

NUMERIC_COLS = ["age","bmi","HbA1c_level","blood_glucose_level"]

def multicollinearity(df: pd.DataFrame, out_path: str):
    corr = df[NUMERIC_COLS].corr(method="pearson")
    warnings = []
    for i,a in enumerate(NUMERIC_COLS):
        for b in NUMERIC_COLS[i+1:]:
            r = corr.loc[a,b]
            if abs(r)>0.8:
                warnings.append(f"⚠️ High correlation between {a} and {b} (r={r:.2f})")
    with open(out_path,"w") as f:
        if warnings: f.write("\n".join(warnings))
        else: f.write("No pairs with |r|>0.8.")