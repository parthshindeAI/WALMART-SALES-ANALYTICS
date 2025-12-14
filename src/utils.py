import pandas as pd

def summarize(df):
    """Returns basic dataframe summary as a dictionary."""
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_total": df.isna().sum().sum(),
        "duplicates": df.duplicated().sum()
    }

def save_clean_version(df, path="data/processed/cleaned.csv"):
    """Save cleaned dataframe."""
    import os
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(path, index=False)
    return path
