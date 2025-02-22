-- 1327. List the Products Ordered in a Period
-- Categories : Database

WITH
    total_units_per_product_of_feb_2020 AS (
SELECT
    product_id,
    SUM(unit) AS total_units
FROM
    Orders
WHERE
    order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY
    product_id
HAVING
    SUM(unit) >= 100)

SELECT
    Products.product_name,
    total_units_per_product_of_feb_2020.total_units AS unit
FROM
    Products
INNER JOIN  
    total_units_per_product_of_feb_2020
ON
    Products.product_id = total_units_per_product_of_feb_2020.product_id;


