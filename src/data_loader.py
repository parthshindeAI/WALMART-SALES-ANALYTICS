import pandas as pd
from pathlib import Path

RAW = Path("data/raw/walmart_full.csv")
SAMPLE = Path("data/sample/walmart_sample.csv")
Path("data/sample").mkdir(parents=True, exist_ok=True)

def create_sample(nrows=10000):
    df = pd.read_csv(RAW)
    df.sample(nrows, random_state=42).to_csv(SAMPLE, index=False)
    print("Sample created at", SAMPLE)

if __name__ == "__main__":
    create_sample()
