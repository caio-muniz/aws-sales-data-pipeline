import pandas as pd


def clean_sales_data(df):
    required_columns = [
        "Order ID",
        "Order Date",
        "Product ID",
        "Sales",
        "Quantity",
        "Profit",
    ]

    df = df.dropna(subset=required_columns).copy()

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        errors="coerce"
    )

    df = df.dropna(subset=["Order Date", "Ship Date"])

    return df