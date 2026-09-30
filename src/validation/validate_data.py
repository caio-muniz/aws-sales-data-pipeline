import pandas as pd


file_path = "data/processed/sales_clean.csv"

df = pd.read_csv(file_path)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])


print("Dimensões:", df.shape)

print("\nValores nulos:")
print(df.isnull().sum())

print("\nDuplicatas:", df.duplicated().sum())

print("Sales <= 0:", (df["Sales"] <= 0).sum())

print("Quantity <= 0:", (df["Quantity"] <= 0).sum())

print(
    "Discount fora de 0-1:",
    ((df["Discount"] < 0) | (df["Discount"] > 1)).sum()
)

print(
    "Ship Date anterior à Order Date:",
    (df["Ship Date"] < df["Order Date"]).sum()
)

print(
    "Profit negativo:",
    (df["Profit"] < 0).sum(),
)