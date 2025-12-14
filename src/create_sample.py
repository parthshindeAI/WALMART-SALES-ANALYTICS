import pandas as pd
from pathlib import Path

# ===============================
# Paths
# ===============================
DATA_DIR = Path("data")
RAW_DIR = DATA_DIR / "raw"
SAMPLE_DIR = DATA_DIR / "sample"

RAW_FILE = RAW_DIR / "walmart_full.csv"
SAMPLE_FILE = SAMPLE_DIR / "walmart_sample.csv"

SAMPLE_DIR.mkdir(parents=True, exist_ok=True)

# ===============================
# Data Creation
# ===============================
def create_sample(nrows: int = 10000, random_state: int = 42) -> None:
    """
    Create a sample dataset from raw Walmart sales data.
    """
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw data not found at {RAW_FILE}")

    df = pd.read_csv(RAW_FILE)
    df.sample(nrows, random_state=random_state).to_csv(SAMPLE_FILE, index=False)
    print(f"Sample created at {SAMPLE_FILE}")

# ===============================
# Data Loading
# ===============================
def load_sample() -> pd.DataFrame:
    """
    Load the sample Walmart dataset.
    """
    if not SAMPLE_FILE.exists():
        raise FileNotFoundError(
            "Sample file not found. Run create_sample() first."
        )
    return pd.read_csv(SAMPLE_FILE)

def load_raw() -> pd.DataFrame:
    """
    Load the full raw Walmart dataset (local only, not for GitHub).
    """
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw data not found at {RAW_FILE}")
    return pd.read_csv(RAW_FILE)

# ===============================
# Script Entry Point
# ===============================
if __name__ == "__main__":
    create_sample()
