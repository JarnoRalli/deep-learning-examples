#Source: https://github.com/lazyprogrammer/financial_engineering/blob/master/append.py
import pandas as pd
from glob import glob

files = glob('data/*.csv')
full_df = None

for f in files:
  print(f'Processing file {f}')
  df = pd.read_csv(f)

  symbol = f.split('/')[1].split('.')[0]
  df['Name'] = symbol

  if full_df is None:
    full_df = df
  else:
    full_df = pd.concat([full_df, df])

full_df.to_csv('sp500full.csv', index=False)
