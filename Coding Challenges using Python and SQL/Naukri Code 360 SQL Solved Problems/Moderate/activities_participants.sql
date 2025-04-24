-- Question: Activity Participants
-- Categories: Moderate

WITH
    activity_and_num_of_participants AS (
SELECT
    Activities.name,
    COUNT(Friends.id) AS number_of_participants
FROM
    Activities
INNER JOIN
    Friends
ON
    Activities.name = Friends.activity
GROUP BY
    Activities.name)

SELECT
    name AS activity
FROM
    activity_and_num_of_participants
WHERE
    number_of_participants <> (SELECT MAX(number_of_participants) FROM activity_and_num_of_participants) AND
    number_of_participants <> (SELECT MIN(number_of_participants) FROM activity_and_num_of_participants);
