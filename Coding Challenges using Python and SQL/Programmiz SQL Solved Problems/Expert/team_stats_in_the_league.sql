-- Question: Write an SQL query to show the stats of teams in the league
-- Categories: Expert

WITH
    team_statistics AS (
SELECT
    team_name,
    matches_played,
    (win_points_as_home_team + win_points_as_away_team + draw_points) AS points,
    (total_goal_as_home_team + total_goal_as_away_team) AS goal_for,
    (total_goal_of_opp_away_team + total_goal_of_opp_home_team) AS goal_against
FROM (
SELECT
    team_name,
    (SELECT COUNT(*) FROM Matches WHERE Matches.home_team_id = Teams.team_id OR Matches.away_team_id = Teams.team_id) AS matches_played,
    (SELECT SUM(CASE WHEN Matches.home_team_goal > Matches.away_team_goal THEN 3 ELSE 0 END) FROM Matches WHERE Matches.home_team_id = Teams.team_id) AS win_points_as_home_team,
    (SELECT SUM(CASE WHEN Matches.away_team_goal > Matches.home_team_goal THEN 3 ELSE 0 END) FROM Matches WHERE Matches.away_team_id = Teams.team_id) AS win_points_as_away_team,
    (SELECT SUM(CASE WHEN Matches.home_team_goal = Matches.away_team_goal THEN 1 ELSE 0 END) FROM Matches WHERE Matches.home_team_id = Teams.team_id OR Matches.away_team_id = Teams.team_id) AS draw_points,
    (SELECT SUM(Matches.home_team_goal) FROM Matches WHERE Matches.home_team_id = Teams.team_id) AS total_goal_as_home_team,
    (SELECT SUM(Matches.away_team_goal) FROM Matches WHERE Matches.away_team_id = Teams.team_id) AS total_goal_as_away_team,
    (SELECT SUM(Matches.away_team_goal) FROM Matches WHERE Matches.home_team_id = Teams.team_id) AS total_goal_of_opp_away_team,
    (SELECT SUM(Matches.home_team_goal) FROM Matches WHERE Matches.away_team_id = Teams.team_id) AS total_goal_of_opp_home_team
FROM
    Teams
) AS team_stats
    )

SELECT
    *,
    (goal_for - goal_against) AS goal_diff
FROM
    team_statistics
ORDER BY
    points DESC,
    goal_diff DESC,
    team_name;