-- Question: Create a Session Bar Chart
-- Categories: Moderate

WITH
    total_session_mins AS (
SELECT
    SUM(CASE WHEN duration >= 0.0 AND duration < 5.0 THEN 1 ELSE 0 END) AS total_session_with_0_to_5_mins,
    SUM(CASE WHEN duration >= 5.0 AND duration < 10.0 THEN 1 ELSE 0 END) AS total_session_with_5_to_10_mins,
    SUM(CASE WHEN duration >= 10.0 AND duration < 15.0 THEN 1 ELSE 0 END) AS total_session_with_10_to_15_mins,
    SUM(CASE WHEN duration >= 15.0 THEN 1 ELSE 0 END) AS total_session_with_15_mins_or_more
FROM (
    SELECT
        session_id,
        duration / 60.0 AS duration
    FROM
        Sessions
) AS duration_mins
    )

SELECT
    '[0-5>' AS bin,
    total_session_with_0_to_5_mins AS total
FROM
    total_session_mins
UNION
SELECT
    '[5-10>' AS bin,
    total_session_with_5_to_10_mins AS total
FROM
    total_session_mins
UNION
SELECT
    '[10-15>' AS bin,
    total_session_with_10_to_15_mins AS total 
FROM
    total_session_mins
UNION
SELECT
    '15 or more' AS bin,
    total_session_with_15_mins_or_more AS total
FROM
    total_session_mins