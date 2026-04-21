import pandas as pd

stocks_df = pd.read_csv('../Data/stocks_data.csv')

gl_df = pd.read_csv('../Data/gainers_losers.csv')

nh_df = pd.read_csv('../Data/new_highs.csv')


len(gl_df[gl_df['security'].isin(stocks_df['security'])]['security'])

len(gl_df['security'])

