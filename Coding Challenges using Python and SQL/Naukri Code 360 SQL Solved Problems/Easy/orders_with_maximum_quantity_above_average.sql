-- Question: Orders With Maximum Quantity Above Average
-- Categories: Easy

WITH
    order_stats AS (
SELECT
    order_id,
    MAX(quantity) AS maximum_quantity,
    (SUM(quantity) * 1.0 ) / COUNT(DISTINCT product_id) AS average_quantity
FROM
    OrdersDetails
GROUP BY
    order_id
    )


SELECT
    order_stats.order_id
FROM
    order_stats
GROUP BY
    order_stats.order_id
HAVING
    MAX(order_stats.maximum_quantity) > (SELECT AVG(inner_table.average_quantity) FROM order_stats AS inner_table);
    