import sqlite3

import pandas as pd


FILE_PATH = "data/processed/sales_clean.csv"
DATABASE_PATH = "data/sales.db"


df = pd.read_csv(FILE_PATH)

connection = sqlite3.connect(DATABASE_PATH)

df.to_sql(
    "sales",
    connection,
    index=False,
    if_exists="replace",
)

customers = (
    df[["Customer ID", "Customer Name", "Segment"]]
    .drop_duplicates(subset=["Customer ID"])
)

customers.to_sql(
    "customers",
    connection,
    index=False,
    if_exists="replace",
)

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM sales")
sales_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM customers")
customers_count = cursor.fetchone()[0]

print(f"Sales records: {sales_count}")
print(f"Customers: {customers_count}")

connection.close()