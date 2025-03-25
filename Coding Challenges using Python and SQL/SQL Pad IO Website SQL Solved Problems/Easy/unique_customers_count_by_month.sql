-- 7.) Unique customers count by month
-- Categories: Easy

SELECT
    EXTRACT(YEAR FROM rental_ts) AS year,
    EXTRACT(MONTH FROM rental_ts) AS mon,
    COUNT(DISTINCT customer_id) AS uu_cnt
FROM
    rental
GROUP BY
    EXTRACT(YEAR FROM rental_ts),
    EXTRACT(MONTH FROM rental_ts);

