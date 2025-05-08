-- Question: Write an SQL query to find players who have consistently been in the top 3 scorers
-- Categories: Expert

WITH
    player_and_season_ranking AS (
SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY season ORDER BY points DESC) AS season_ranking
FROM
    PlayerStats
ORDER BY
    season
    )

SELECT
    Teams.player_name,
    Teams.team,
    Teams.city,
    COUNT(player_and_season_ranking.player_id) AS top3_count
FROM
    Teams
INNER JOIN
    player_and_season_ranking
ON
    Teams.player_id = player_and_season_ranking.player_id
WHERE
    player_and_season_ranking.season_ranking BETWEEN 1 AND 3
GROUP BY
    Teams.player_name,
    Teams.team,
    Teams.city
HAVING
    COUNT(player_and_season_ranking.player_id) > 1;
