-- Question: Write an SQL query to determine whether a salesman has reached his annual quota
-- Categories: Medium

SELECT
    Deals.employee_id,
    CASE
        WHEN SUM(Deals.deal_size) >= Quotas.quota THEN 'yes'
        ELSE 'no'
    END AS made_quota
FROM
    Deals
INNER JOIN
    Quotas
ON
    Deals.employee_id = Quotas.employee_id
GROUP BY
    Deals.employee_id;
