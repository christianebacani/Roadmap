-- Question: Write an SQL query to find the total units for each product where the combined sales exceeded 100 units
-- Categories: Medium

SELECT
    product_name,
    SUM(units_sold) AS total_sales
FROM
    Sales
GROUP BY
    product_name
HAVING
    SUM(units_sold) > 100;
