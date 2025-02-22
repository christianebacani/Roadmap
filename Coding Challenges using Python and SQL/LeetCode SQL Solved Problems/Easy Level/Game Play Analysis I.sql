-- 511. Game Play Analysis I 
-- Categories : Database

WITH
    login_logs AS (
SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS login_rank
FROM
    Activity)

SELECT
    player_id,
    event_date AS first_login
FROM
    login_logs
WHERE
    login_rank = 1;

