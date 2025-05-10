-- Question: Top Travellers
-- Categories: Hard

WITH
    total_distance_travelled_per_users AS (
SELECT
    DISTINCT
    Users.name,
    COALESCE((SELECT SUM(Inner_Table.distance) FROM Rides AS Inner_Table WHERE Inner_Table.user_id = Users.id), 0) AS travelled_distance
FROM
    Users
LEFT JOIN
    Rides
ON
    Users.id = Rides.user_id
    )

SELECT
    name,
    travelled_distance
FROM
    total_distance_travelled_per_users
ORDER BY
    travelled_distance DESC,
    name ASC;