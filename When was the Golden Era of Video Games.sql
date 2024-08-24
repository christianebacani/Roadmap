-- Database Name
USE practicedb;
-- I am a Data Engineer!

-- best_selling_games
SELECT *
FROM game_sales
ORDER BY games_sold DESC
LIMIT 10;


-- critics_top_ten_years
SELECT
	year,
    COUNT(name) AS num_games,
    ROUND(AVG(critic_score), 2) AS avg_critic_score
FROM game_sales AS g
INNER JOIN game_reviews AS r
	USING(name) 
GROUP BY year
HAVING COUNT(name) > 4
ORDER BY avg_critic_score DESC
LIMIT 10;


-- golden_years
SELECT 
	u.year AS year, 
    c.num_games AS num_games,
    avg_critic_score,
    avg_user_score,
    ROUND((avg_critic_score - avg_user_score), 2) AS diff
FROM users_avg_year_rating AS u
INNER JOIN critics_avg_year_rating AS c
	USING(year)
WHERE avg_user_score > 9 OR avg_critic_score > 9
ORDER BY year DESC;


    
    
    
    
    
    
    






