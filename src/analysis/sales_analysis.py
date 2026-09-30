import pandas as pd

file_path = "data/processed/sales_clean.csv"

df = pd.read_csv(file_path)

df['Month'] = pd.to_datetime(df['Order Date'])

faturamento_mes = df.groupby(pd.Grouper(key='Month', freq="ME"))['Sales'].sum().reset_index()

print("---Faturamento por mes---\n", faturamento_mes)

print(df['Category'])
