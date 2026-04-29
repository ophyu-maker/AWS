import pandas as pd
from pathlib import Path


INPUT_FILE = Path("SAU-HighSeas-71-v48-0.csv")
OUTPUT_FILE = Path("SAU-HighSeas-71-v48-0.parquet")


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)

    print("High Seas CSV loaded successfully.")
    print(f"Rows: {len(df):,}")
    print("Columns:")
    print(df.columns.tolist())

    df.to_parquet(OUTPUT_FILE, index=False)

    print(f"Parquet file created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
