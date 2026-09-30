import pandas as pd

from src.transformation.clean_data import clean_sales_data


file_path = "data/raw/Superstore.csv"
output_path = "data/processed/sales_clean.csv"

df = pd.read_csv(file_path)

print("Dados originais:", df.shape)

clean_df = clean_sales_data(df)

print("Dados após limpeza:", clean_df.shape)

clean_df.to_csv(output_path, index=False)

print(f"\nArquivo salvo em: {output_path}")