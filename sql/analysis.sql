-- 1. Quantidade de registros
SELECT COUNT(*)
FROM sales;


-- 2. Faturamento total
SELECT SUM(Sales) AS total_sales
FROM sales;


-- 3. Faturamento por categoria
SELECT
    Category,
    SUM(Sales) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;


-- 4. Lucro total por categoria
SELECT
    Category,
    SUM(Profit) AS total_profit
FROM sales
GROUP BY Category
ORDER BY total_profit DESC;


-- 5. Vendas por região
SELECT
    Region,
    SUM(Sales) AS total_sales
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;


-- 6. Produtos mais vendidos em faturamento
SELECT
    "Product Name",
    SUM(Sales) AS total_sales
FROM sales
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10;