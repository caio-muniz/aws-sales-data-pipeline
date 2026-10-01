from pyspark.sql import SparkSession
import pyspark.sql.functions as F


FILE_PATH = "data/processed/sales_clean.csv"


spark = (
    SparkSession.builder
    .appName("PySpark Sales Analysis")
    .getOrCreate()
)


df = spark.read.csv(
    FILE_PATH,
    header=True,
    inferSchema=True,
    escape='"'
)

df.printSchema()
df.select("Sales", "Profit").show(20)

monthly_sales = (
    df.withColumn(
        "month",
        F.date_trunc("month", "Order Date")
    )
    .groupBy("month")
    .agg(
        F.sum("Sales").alias("total_sales")
    )
    .orderBy("month")
)


print("\n--- Monthly Sales ---")
monthly_sales.show()


category_performance = (
    df.groupBy("Category")
    .agg(
        F.sum("Sales").alias("total_sales"),
        F.sum("Profit").alias("total_profit"),
    )
    .orderBy(F.desc("total_sales"))
)


print("\n--- Category Performance ---")
category_performance.show()


spark.stop()