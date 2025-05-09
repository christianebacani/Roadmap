-- Question: Write an SQL query to alter the table
-- Categories: Expert

SELECT
    order_id,
    ROUND(total_amount) AS total_amount,
    (8 * total_amount) / 100 AS sales_tax
FROM
    Orders;