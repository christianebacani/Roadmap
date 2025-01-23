-- 584. Find Customer Referee
-- Category : Database

SELECT
    name
FROM
    Customer
WHERE
    referee_id IS NULL OR
    referee_id <> 2;
    