import sqlite3
import pandas as pd

file_path = "data/processed/sales_clean.csv"

df = pd.read_csv(file_path)

conexao = sqlite3.connect("data/sales.db")

df.to_sql('sales', conexao, index=False, if_exists='replace')

conexao.close()

conexao = sqlite3.connect("data/sales.db")
cursor = conexao.cursor()

cursor.execute("SELECT COUNT(*) FROM sales")
resultado = cursor.fetchall()

print(resultado)

conexao.close()
