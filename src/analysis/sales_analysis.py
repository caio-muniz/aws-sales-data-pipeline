import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/processed/sales_clean.csv"

df = pd.read_csv(file_path)

df['Month'] = pd.to_datetime(df['Order Date'])

faturamento_mes = df.groupby(pd.Grouper(key='Month', freq="ME"))['Sales'].sum().reset_index()

print("---Faturamento por mes---\n", faturamento_mes)

faturamento_mes.plot(x='Month', y='Sales')
plt.title("Faturamento por mes")
plt.xlabel("Month")
plt.ylabel("Sales")


categories = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()
categories = categories.sort_values('Profit', ascending=False)
print("\n---Categorias lucrativas---\n", categories)


discount = df.groupby('Discount')['Profit'].mean().reset_index()
discount.rename(columns={'Profit' : 'Mean Profit'}, inplace=True)

print("\n---Discounts---\n", discount)

discount.plot(x= 'Discount', y='Mean Profit')
plt.title("Descontos")
plt.xlabel("Discount")
plt.ylabel("Mean Profit")

plt.show()