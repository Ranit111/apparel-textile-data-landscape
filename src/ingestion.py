from pathlib import Path
import pandas as pd

RAW = Path("data/raw")

def load_eea_indicators():
    path = RAW / "eea_textile_indicators.csv"
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path)

if __name__ == "__main__":
    df = load_eea_indicators()
    print(f"Loaded {len(df)} official EEA textile indicators.")
    print(df[["indicator", "year", "value", "unit"]].to_string(index=False))
