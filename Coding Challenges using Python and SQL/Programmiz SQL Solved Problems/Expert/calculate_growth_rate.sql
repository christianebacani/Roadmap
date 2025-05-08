-- Question: Write an SQL query to calculate each top-selling product's monthly revenue growth rate
-- Categories: Expert

WITH
    products_current_and_past_revenue AS (
SELECT
    DISTINCT
    Products.product_name,
    (SELECT CONCAT(SUBSTRING(CAST(Inner_Table.sale_date AS VARCHAR), 1, 4), '-', SUBSTRING(CAST(Inner_Table.sale_date AS VARCHAR), 6, 2)) FROM Sales AS Inner_Table WHERE Inner_Table.product_id = Products.product_id ORDER BY sale_date DESC LIMIT 1
    ) AS month,
    (SELECT Inner_Table.revenue FROM Sales AS Inner_Table WHERE Inner_Table.product_id = Products.product_id ORDER BY Inner_Table.sale_date DESC LIMIT 1) AS revenue,
    (SELECT Inner_Table.revenue FROM Sales AS Inner_Table WHERE Inner_Table.product_id = Products.product_id ORDER BY Inner_Table.sale_date DESC LIMIT 1 OFFSET 1) AS revenue_last_month
FROM
    Products
INNER JOIN
    Sales
ON
    Products.product_id = Sales.product_id
    )

SELECT
    *,
    CONCAT(((revenue - revenue_last_month) / (revenue_last_month * 1.00)) * 100.00, '0%') AS growth_rate
FROM
    products_current_and_past_revenue;