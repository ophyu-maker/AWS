import pandas as pd
from pathlib import Path


INPUT_FILE = Path("SAU-EEZ-242-v48-0.csv")
BACKUP_FILE = Path("SAU-EEZ-242-v48-0-old.csv")
OUTPUT_CSV = Path("SAU-EEZ-242-v48-0-cleaned.csv")
OUTPUT_PARQUET = Path("SAU-EEZ-242-v48-0.parquet")


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)

    print("EEZ CSV loaded successfully.")
    print(f"Rows: {len(df):,}")

    print("\nOriginal columns:")
    print(df.columns.tolist())

    df.to_csv(BACKUP_FILE, index=False)

    df.rename(
        columns={
            "fish_name": "common_name",
            "country": "fishing_entity"
        },
        inplace=True
    )

    print("\nUpdated columns:")
    print(df.columns.tolist())

    df.to_csv(OUTPUT_CSV, index=False)
    df.to_parquet(OUTPUT_PARQUET, index=False)

    print(f"\nBackup CSV created: {BACKUP_FILE}")
    print(f"Cleaned CSV created: {OUTPUT_CSV}")
    print(f"Parquet file created: {OUTPUT_PARQUET}")


if __name__ == "__main__":
    main()
