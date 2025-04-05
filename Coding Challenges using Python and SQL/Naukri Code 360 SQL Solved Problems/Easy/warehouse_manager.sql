-- Question: Warehouse Manager
-- Categories: Easy

WITH
    warehouse_volumes AS (
SELECT
    Warehouse.name AS warehouse_name,
    (Products.Width * Products.Length * Products.Height) * Warehouse.units AS volume
FROM
    Warehouse
INNER JOIN
    Products
ON
    Warehouse.product_id = Products.product_id
    )

SELECT
    warehouse_name,
    SUM(volume) AS volume
FROM
    warehouse_volumes
GROUP BY
    warehouse_name;