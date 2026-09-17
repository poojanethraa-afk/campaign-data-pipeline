import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path(__file__).resolve().parent / "data" / "german_credit_data.csv"

def extract_data(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path, index_col=0)
    print(f"Extracted {len(df)} rows, {len(df.columns)} columns from {path.name}")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())
    print(df.columns.tolist())
