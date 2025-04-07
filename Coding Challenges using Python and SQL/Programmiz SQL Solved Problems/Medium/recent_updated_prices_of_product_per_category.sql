-- Question: Write an SQL query to retrieve the most recent price for each category
-- Categories: Medium

WITH
    product_and_recent_updated_rankings_per_category AS (
SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY updated_at DESC) AS recent_updated_ranking
FROM
    Products
    )

SELECT
    category,
    price,
    updated_at
FROM
    product_and_recent_updated_rankings_per_category
WHERE
    recent_updated_ranking = 1
ORDER BY
    category;

    