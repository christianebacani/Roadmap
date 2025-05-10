-- Question: Get the Second Most Recent Activity
-- Categories: Hard

WITH
    username_and_activity_rankings AS (
SELECT
    username,
    activity,
    startDate,
    endDate,
    ROW_NUMBER() OVER (PARTITION BY username ORDER BY startDate DESC) AS activity_ranking
FROM
    UserActivity
    )

SELECT
    username,
    activity,
    startDate,
    endDate
FROM
    username_and_activity_rankings
WHERE
    activity_ranking = 2
UNION ALL
SELECT
    username,
    activity,
    startDate,
    endDate
FROM
    username_and_activity_rankings
WHERE
    activity_ranking = 1 AND
    (SELECT COUNT(Inner_Table.activity_ranking) FROM username_and_activity_rankings AS Inner_Table WHERE Inner_Table.username = username_and_activity_rankings.username) = 1;
