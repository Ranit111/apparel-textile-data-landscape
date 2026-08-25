from pathlib import Path
import pandas as pd

RAW = Path("data/raw")
PROCESSED = Path("data/processed")
PROCESSED.mkdir(parents=True, exist_ok=True)

def clean_eea_indicators(df):
    df = df.copy()
    df["indicator"] = df["indicator"].astype("string").str.strip()
    df["source"] = df["source"].astype("string").str.strip()
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    df["missing_flag"] = df["value"].isna()
    df["source_verified"] = df["source_url"].astype("string").str.startswith(
        "https://www.eea.europa.eu/"
    )
    return df

if __name__ == "__main__":
    path = RAW / "eea_textile_indicators.csv"
    df = pd.read_csv(path)
    clean = clean_eea_indicators(df)
    out = PROCESSED / "eea_textile_indicators_clean.csv"
    clean.to_csv(out, index=False)
    print(f"Wrote {out} ({len(clean)} rows)")
