-- Question: Write an SQl query to find shows that did not air on the same date as GOT's 'Baelor' episode
-- Categories: Hard

WITH
    got_baelor_episode_air_date AS (
SELECT
    air_date
FROM
    Shows
WHERE
    title = 'GOT' AND
    episode_name = 'Baelor'
    )

SELECT
    Shows.title,
    Shows.episode_name
FROM
    got_baelor_episode_air_date
INNER JOIN
    Shows
ON
    got_baelor_episode_air_date.air_date <> Shows.air_date;