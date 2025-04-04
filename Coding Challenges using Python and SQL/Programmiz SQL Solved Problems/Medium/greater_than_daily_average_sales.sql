-- Question: Write an SQL query to return the list of products sold each day that exceeded the daily average sales
-- Categories: Medium

WITH
    daily_average_sales AS (
SELECT
    *,
    (SELECT AVG(Inner_Table.units_sold) FROM Sales AS Inner_Table WHERE Inner_Table.date = Sales.date) AS daily_average_sale
FROM
    Sales
    )

SELECT
    date,
    product_name,
    units_sold
FROM
    daily_average_sales
WHERE
    units_sold > daily_average_sale;


