-- Question: Fix the Issue
-- Categories: Moderate

WITH
    formatted_sales AS (
SELECT
    sale_id,
    LOWER(TRIM(product_name)) AS product_name,
    SUBSTRING(CAST(sale_date AS VARCHAR), 1, 7) AS sale_date
FROM
    Sales)

SELECT
    product_name,
    sale_date,
    COUNT(*) AS total
FROM
    formatted_sales
GROUP BY
    product_name,
    sale_date
ORDER BY
    product_name ASC,
    sale_date ASC;
