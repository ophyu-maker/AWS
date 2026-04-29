import pandas as pd

df = pd.read_csv('SAU-HighSeas-71-v48-0.csv')
df.to_parquet('SAU-HighSeas-71-v48-0.parquet')
