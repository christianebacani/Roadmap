-- Question: Write an SQL query to find the total number of fruits sold on each day
-- Categories: Medium

SELECT
    sales_date,
    SUM(quantity) AS total_fruits_sold
FROM
    Fruits
GROUP BY
    sales_date
