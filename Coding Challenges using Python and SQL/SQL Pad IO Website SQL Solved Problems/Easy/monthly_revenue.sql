-- 5.) Monthly revenue
-- Categories: Easy

SELECT
    EXTRACT(YEAR FROM payment_ts) AS year,
    EXTRACT(MONTH FROM payment_ts) AS month,
    ROUND(SUM(amount), 2) AS amount
FROM
    payment
GROUP BY
    EXTRACT(YEAR FROM payment_ts),
    EXTRACT(MONTH FROM payment_ts);

