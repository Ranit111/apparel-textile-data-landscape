from pathlib import Path
import pandas as pd

PROCESSED = Path("data/processed")
OUTPUT = Path("outputs/tables")
OUTPUT.mkdir(parents=True, exist_ok=True)

def percentage_indicators(df):
    return df[df["unit"] == "%"].sort_values("value", ascending=False)

if __name__ == "__main__":
    df = pd.read_csv(PROCESSED / "eea_textile_indicators_clean.csv")
    pct = percentage_indicators(df)
    pct.to_csv(OUTPUT / "percentage_indicators.csv", index=False)
    print(pct[["indicator","year","value","unit"]].to_string(index=False))
