# Make a backup of the file before you modify it in place
cp SAU-EEZ-242-v48-0.csv SAU-EEZ-242-v48-0-old.csv

import pandas as pd

# Load the backup version of the EEZ file
data_location = 'SAU-EEZ-242-v48-0-old.csv'

# Read the CSV into a dataframe
df = pd.read_csv(data_location)

# View the current column names / first row before rename
print(df.head(1))

# Rename EEZ columns to match the other datasets
df.rename(
    columns={
        "fish_name": "common_name",
        "country": "fishing_entity"
    },
    inplace=True
)

# Verify the column names after rename
print(df.head(1))

# Write the cleaned file to CSV and Parquet
df.to_csv('SAU-EEZ-242-v48-0.csv', header=True, index=False)
df.to_parquet('SAU-EEZ-242-v48-0.parquet')
