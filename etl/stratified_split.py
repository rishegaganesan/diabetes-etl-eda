from sklearn.model_selection import train_test_split
import pandas as pd

TARGET = "diabetes"

def stratified_split(df: pd.DataFrame, seed=42, test_size=0.2, valid_size=0.1):
    """
    Performs stratified train/valid/test split on the target column (diabetes).
    Falls back gracefully if stratification is not feasible.
    """

    y = df[TARGET]

    # Check if stratification is feasible
    value_counts = y.value_counts()
    can_stratify = len(value_counts) >= 2 and value_counts.min() >= 2
    stratify_main = y if can_stratify else None

    # First: train/test split
    train_df, test_df = train_test_split(
        df,
        test_size=test_size,
        stratify=stratify_main,
        random_state=seed
    )

    # Recalculate target for the training subset
    y_train = train_df[TARGET]
    value_counts_train = y_train.value_counts()
    can_stratify_train = len(value_counts_train) >= 2 and value_counts_train.min() >= 2
    stratify_valid = y_train if can_stratify_train else None

    # Compute validation fraction relative to remaining train set
    valid_rel = valid_size / (1 - test_size)
    valid_rel = min(max(valid_rel, 0.01), 0.5)  # safety clamp

    # Second: train/valid split
    train_df, valid_df = train_test_split(
        train_df,
        test_size=valid_rel,
        stratify=stratify_valid,
        random_state=seed
    )

    return train_df, valid_df, test_df