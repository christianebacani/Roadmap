-- 2.) Top 3 movie categories by sales
-- Categories: Easy

SELECT
    category
FROM
    sales_by_film_category
ORDER BY
    total_sales DESC
LIMIT
    3;
