import pandas as pd
import matplotlib.pyplot as plt


FILE_PATH = "data/processed/sales_clean.csv"


# Load data
df = pd.read_csv(FILE_PATH)

df["Order Date"] = pd.to_datetime(df["Order Date"])


# 1. Monthly revenue
monthly_sales = (
    df.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"]
    .sum()
    .reset_index()
)

print("\n--- Monthly Revenue ---")
print(monthly_sales)

monthly_sales.plot(
    x="Order Date",
    y="Sales",
    kind="line",
    title="Monthly Revenue",
    xlabel="Month",
    ylabel="Sales",
    legend=False,
)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. Category performance
categories = (
    df.groupby("Category")[["Sales", "Profit"]]
    .sum()
    .reset_index()
    .sort_values("Profit", ascending=False)
)

print("\n--- Category Performance ---")
print(categories)

categories.plot(
    x="Category",
    y=["Sales", "Profit"],
    kind="bar",
    title="Sales and Profit by Category",
    xlabel="Category",
    ylabel="Amount",
)

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 3. Discount vs. average profit
discount_analysis = (
    df.groupby("Discount")["Profit"]
    .mean()
    .reset_index(name="Mean Profit")
)

print("\n--- Discount vs. Mean Profit ---")
print(discount_analysis)

discount_analysis.plot(
    x="Discount",
    y="Mean Profit",
    kind="line",
    marker="o",
    title="Discount vs. Mean Profit",
    xlabel="Discount",
    ylabel="Mean Profit",
    legend=False,
)

plt.tight_layout()
plt.show()


# 4. Product performance
products = (
    df.groupby("Product Name")[["Sales", "Profit"]]
    .sum()
    .reset_index()
)

products["Profit Margin"] = (
    products["Profit"] / products["Sales"]
) * 100

top_products = (
    products
    .sort_values("Sales", ascending=False)
    .head(10)
)

print("\n--- Top 10 Products by Sales ---")
print(top_products)


# 5. Regional performance
regions = (
    df.groupby("Region")[["Sales", "Profit"]]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)

print("\n--- Regional Performance ---")
print(regions)


# 6. Orders and average order value
total_sales = df["Sales"].sum()
total_orders = df["Order ID"].nunique()
average_order_value = total_sales / total_orders

print("\n--- General Metrics ---")
print(f"Total sales: ${total_sales:,.2f}")
print(f"Total orders: {total_orders:,}")
print(f"Average order value: ${average_order_value:,.2f}")