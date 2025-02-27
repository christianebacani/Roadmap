-- 1174. Immediate Food Delivery II
-- Categories : Database

WITH    
    order_ranks AS (
SELECT
    customer_id,
    order_date,
    customer_pref_delivery_date,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS order_rank
FROM
    Delivery
)


SELECT
    ROUND(COUNT(customer_id) / (SELECT COUNT(*) FROM order_ranks AS inner_table WHERE inner_table.order_rank = 1) * 100, 2) AS immediate_percentage
FROM
    order_ranks
WHERE
    order_rank = 1 AND
    order_date = customer_pref_delivery_date;

