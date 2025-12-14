import pandas as pd

def clean_columns(df):
    """Standardize column names to snake_case."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

def convert_date(df, date_col="date"):
    """Convert date column to datetime & extract useful components."""
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month
    df["day"] = df[date_col].dt.day
    df["year_month"] = df[date_col].dt.to_period("M")
    return df

def handle_missing(df, strategy="simple"):
    """
    Handles missing values depending on strategy.
    Strategies:
        - simple: forward fill
        - drop: drop NA rows
        - median: fill numeric columns with median
    """
    if strategy == "simple":
        return df.fillna(method="ffill").fillna(method="bfill")
    elif strategy == "drop":
        return df.dropna()
    elif strategy == "median":
        for c in df.select_dtypes("number").columns:
            df[c] = df[c].fillna(df[c].median())
        return df
    else:
        raise ValueError("Unknown strategy")

def basic_outlier_handling(df, column):
    """Remove extreme outliers using z-score method."""
    mean = df[column].mean()
    std = df[column].std()
    df = df[(df[column] > mean - 3*std) & (df[column] < mean + 3*std)]
    return df
