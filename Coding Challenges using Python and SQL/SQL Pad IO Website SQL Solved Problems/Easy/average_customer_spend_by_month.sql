-- 8.) Average customer spend by month
-- Categories: Easy

SELECT
    EXTRACT(YEAR FROM payment_ts) AS year,
    EXTRACT(MONTH FROM payment_ts) as mon,
    SUM(amount) / COUNT(DISTINCT customer_id) AS avg_spend
FROM
    payment
GROUP BY
    EXTRACT(YEAR FROM payment_ts),
    EXTRACT(MONTH FROM payment_ts);
