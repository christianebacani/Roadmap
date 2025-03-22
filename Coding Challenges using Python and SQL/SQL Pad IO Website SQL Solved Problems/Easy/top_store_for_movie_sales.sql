-- 1.) Top store for movie sales
-- Categories: Easy

SELECT
    store,
    manager
FROM
    sales_by_store
ORDER BY
    total_sales DESC
LIMIT
    1;

