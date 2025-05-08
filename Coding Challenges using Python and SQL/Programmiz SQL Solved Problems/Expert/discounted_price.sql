-- Question: Write an SQL query to add a column discount
-- Categories: Expert

WITH
    product_and_discounts AS (
SELECT
    product_id,
    product_name,
    price,
    stock,
    CASE
        WHEN product_name = 'Laptop' THEN 0.1
        WHEN product_name = 'Smartphone' THEN 0.05
    END AS discount
FROM
    Products
    )

SELECT
    product_id,
    product_name,
    price - (discount * price) AS price,
    stock,
    discount
FROM
    product_and_discounts;