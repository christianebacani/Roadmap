-- Question: Customers Who Bought All Products
-- Categories: Moderate

WITH
    customer_and_total_products_bought AS (
SELECT
    DISTINCT
    customer_id,
    (SELECT COUNT(DISTINCT Inner_Table.product_key) FROM Customer AS Inner_Table WHERE Inner_Table.customer_id = Customer.customer_id) AS total_products_bought
FROM
    Customer
    )

SELECT
    customer_id
FROM
    customer_and_total_products_bought
WHERE
    total_products_bought = (SELECT COUNT(*) FROM Product);