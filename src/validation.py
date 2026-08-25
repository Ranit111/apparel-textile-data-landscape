from pathlib import Path
import pandas as pd

PROCESSED = Path("data/processed")
OUTPUT = Path("outputs/tables")
OUTPUT.mkdir(parents=True, exist_ok=True)

REQUIRED = ["indicator","year","value","unit","geography","source","source_url"]

def validate(df):
    missing_columns = [c for c in REQUIRED if c not in df.columns]
    return {
        "rows": len(df),
        "missing_columns": ", ".join(missing_columns),
        "missing_values": int(df["value"].isna().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "unverified_sources": int((~df["source_url"].astype(str).str.startswith(
            "https://www.eea.europa.eu/"
        )).sum())
    }

if __name__ == "__main__":
    path = PROCESSED / "eea_textile_indicators_clean.csv"
    df = pd.read_csv(path)
    result = validate(df)
    pd.DataFrame([result]).to_csv(OUTPUT / "validation_summary.csv", index=False)
    print(result)
