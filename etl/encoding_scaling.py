from sklearn.preprocessing import StandardScaler
import pandas as pd

NUMERIC_COLS = ["age","bmi","HbA1c_level","blood_glucose_level"]

def encode_and_scale(df: pd.DataFrame):
    df = pd.get_dummies(df, columns=["gender","smoking_history"], drop_first=False, dtype=int)
    scaler = StandardScaler()
    df[NUMERIC_COLS] = scaler.fit_transform(df[NUMERIC_COLS])
    return df