-- Question: Customer Placing the Largest Number Orders
-- Categories: Easy

WITH
    number_of_orders AS (
SELECT
    customer_number,
    COUNT(order_number) AS order_count
FROM
    Orders
GROUP BY
    customer_number
    )

SELECT
    customer_number
FROM
    number_of_orders
ORDER BY
    order_count DESC
LIMIT
    1;
