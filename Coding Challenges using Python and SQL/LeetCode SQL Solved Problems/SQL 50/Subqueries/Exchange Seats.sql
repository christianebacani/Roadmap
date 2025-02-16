-- 626. Exchange Seats
-- Categories : Database

WITH
    consecutive_ids AS (
SELECT
    id,
    CASE 
        WHEN id % 2 != 0 THEN LEAD(id, 1, id) OVER (ORDER BY id)
        ELSE LAG(id, 1) OVER (ORDER BY id)
    END AS swapped_id,
    student
FROM
    Seat)

SELECT
    swapped_id AS id,
    student
FROM
    consecutive_ids
ORDER BY
    id;
