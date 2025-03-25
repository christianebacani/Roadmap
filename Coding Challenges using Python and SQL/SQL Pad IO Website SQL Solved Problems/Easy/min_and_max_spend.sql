-- 10.) Min and max spend
-- Categories: Easy

WITH
    total_spends AS (
SELECT
    SUM(amount) AS total_spent
FROM
    payment
WHERE
    EXTRACT(YEAR FROM payment_ts) = 2020 AND
    EXTRACT(MONTH FROM payment_ts) = 06
GROUP BY
    customer_id
    )

SELECT
    MIN(total_spent) AS min_spend,
    MAX(total_spent) AS max_spend
FROM
    total_spends;

