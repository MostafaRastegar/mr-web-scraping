import pandas as pd

df = pd.read_csv('snapp-market.csv')

print(df.to_string())

print(df.info())
