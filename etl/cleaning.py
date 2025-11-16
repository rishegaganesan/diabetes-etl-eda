import numpy as np
import pandas as pd

ALLOWED_SMOKING = {"current", "ever", "former", "never", "No Info", "not current"}
NUMERIC_COLS = ["age", "bmi", "HbA1c_level", "blood_glucose_level"]
QUARANTINE_REASON = "_quarantine_reason"

def clean_data(df: pd.DataFrame):
    df = df.copy()
    df["gender"] = df["gender"].astype(str).str.strip().str.title()
    df["smoking_history"] = df["smoking_history"].astype(str).str.strip()

    reasons = []
    reasons.append((df[NUMERIC_COLS].isna().any(axis=1), "missing_required_values"))
    reasons.append((~df["smoking_history"].isin(ALLOWED_SMOKING), "smoking_history_invalid"))
    reasons.append((~df["gender"].isin({"Male","Female","Other"}), "gender_invalid"))
    reasons.append((df["age"].lt(0) | df["age"].gt(120), "age_out_of_range"))

    quarantine_mask = False
    for mask,_ in reasons: quarantine_mask |= mask

    quarantine_df = df.loc[quarantine_mask].copy()
    if not quarantine_df.empty:
        reasons_per_row = {i: [] for i in quarantine_df.index}
        for mask, name in reasons:
            for idx in quarantine_df.index:
                if mask.loc[idx]:
                    reasons_per_row[idx].append(name)
        quarantine_df[QUARANTINE_REASON] = pd.Series({i: ";".join(v) for i,v in reasons_per_row.items()})

    clean_df = df.loc[~quarantine_mask].copy()
    return clean_df, quarantine_df