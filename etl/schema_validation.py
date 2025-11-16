import pandas as pd

EXPECTED_COLUMNS = [
    "gender", "age", "hypertension", "heart_disease",
    "smoking_history", "bmi", "HbA1c_level",
    "blood_glucose_level", "diabetes"
]

def validate_schema(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df[EXPECTED_COLUMNS]