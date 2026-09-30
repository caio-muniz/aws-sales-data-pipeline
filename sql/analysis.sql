-- 1. Sales and profit by customer segment
SELECT
    customers."Segment",
    SUM(sales."Sales") AS total_sales,
    SUM(sales."Profit") AS total_profit
FROM sales
JOIN customers
    ON sales."Customer ID" = customers."Customer ID"
GROUP BY customers."Segment"
ORDER BY total_sales DESC;


-- 2. Sales by customer segment using a CTE
WITH segment_sales AS (
    SELECT
        customers."Segment",
        SUM(sales."Sales") AS total_sales,
        SUM(sales."Profit") AS total_profit
    FROM sales
    JOIN customers
        ON sales."Customer ID" = customers."Customer ID"
    GROUP BY customers."Segment"
)
SELECT
    "Segment",
    total_sales,
    total_profit
FROM segment_sales
ORDER BY total_sales DESC;


-- 3. Top 10 products by sales
WITH product_sales AS (
    SELECT
        "Product Name",
        SUM("Sales") AS total_sales
    FROM sales
    GROUP BY "Product Name"
)
SELECT
    "Product Name",
    total_sales,
    RANK() OVER (
        ORDER BY total_sales DESC
    ) AS sales_rank
FROM product_sales
ORDER BY sales_rank
LIMIT 10;