-- 180. Consecutive Numbers
-- Categories : Database

WITH
    id_and_consecutive_nums AS (
SELECT
    num AS first_num,
    LEAD(num, 1) OVER (ORDER BY id) AS second_num,
    LEAD(num, 2) OVER (ORDER BY id) AS third_num
FROM
    Logs)

SELECT
    DISTINCT first_num AS ConsecutiveNums
FROM
    id_and_consecutive_nums
WHERE
    first_num = second_num AND
    second_num = third_num;
