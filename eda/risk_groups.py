import pandas as pd
import numpy as np

def risk_groups(df: pd.DataFrame, out_path: str):
    cohorts = [
        ("Elderly", df["age"]>=60, "age ≥ 60"),
        ("Overweight", df["bmi"]>=30, "BMI ≥ 30"),
        ("Hypertension", df["hypertension"]==1, "hypertension = 1"),
        ("Heart Disease", df["heart_disease"]==1, "heart_disease = 1"),
        ("High Glucose", df["blood_glucose_level"]>=180, "blood_glucose_level ≥ 180"),
        ("Smokers", df["smoking_history"].isin({"current","ever","former","not current"}), 
         "smoking_history ∈ {current, ever, former, not current}")
    ]
    rows = []
    for name,mask,cond in cohorts:
        sub=df[mask]
        rows.append({"Cohort":name,"Condition":cond,"N":len(sub),"Diabetes %":sub["diabetes"].mean()*100 if len(sub)>0 else np.nan})
    pd.DataFrame(rows).to_csv(out_path,index=False)