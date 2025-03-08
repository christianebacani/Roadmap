-- Basic Commands: Player Details

SELECT
    Matches.match_id,
    Matches.player_1,
    Matches.player_2,
    Players.player_name AS winner,
    Matches.match_date,
    Players.score
FROM
    Players
INNER JOIN 
    Matches
ON
    Players.player_name = Matches.winner
ORDER BY
    Matches.match_date DESC
LIMIT
    5;
