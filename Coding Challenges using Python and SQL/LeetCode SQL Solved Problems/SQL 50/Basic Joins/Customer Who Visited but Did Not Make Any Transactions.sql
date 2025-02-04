-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- Category : Database

SELECT
    Visits.customer_id,
    COUNT(Visits.customer_id) AS count_no_trans
FROM
    Visits
LEFT JOIN
    Transactions
ON
    Visits.visit_id = Transactions.visit_id
WHERE
    Transactions.visit_id IS NULL
GROUP BY
    Visits.customer_id;
    
