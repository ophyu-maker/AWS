import pandas as pd

df = pd.read_csv('SAU-GLOBAL-1-v48-0.csv')
df.to_parquet('SAU-GLOBAL-1-v48-0.parquet')
