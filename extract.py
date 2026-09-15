import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/marketing_campaign.csv")

def extract_data(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path, sep=";")
    print(f"Extracted {len(df)} rows, {len(df.columns)} columns from {path.name}")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())
    print(df.columns.tolist())
