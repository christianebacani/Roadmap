-- Question: The Latest Login in 2020
-- Categories: Moderate

WITH
    user_id_and_last_stamp AS (
SELECT
    DISTINCT
    user_id,
    (SELECT time_stamp FROM Logins AS Inner_Table WHERE Inner_Table.user_id = Logins.user_id AND EXTRACT(YEAR FROM Inner_Table.time_stamp) = '2020' ORDER BY time_stamp DESC LIMIT 1) AS last_stamp
FROM
    Logins)

SELECT
    user_id,
    last_stamp
FROM
    user_id_and_last_stamp
WHERE
    last_stamp IS NOT NULL;