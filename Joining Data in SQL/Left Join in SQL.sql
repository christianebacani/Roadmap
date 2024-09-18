-- Use any database 
USE countries;


-- Left Join in MySQL

-- Create
CREATE TABLE seasons(season_id INT PRIMARY KEY,
						season_name VARCHAR(50));

CREATE TABLE tournaments(tournament_id INT PRIMARY KEY,
							season_id INT,
                            tournament_name VARCHAR(50));
-- Insert
INSERT INTO seasons(season_id,
					season_name) 
VALUES (1, 'Summer 2024'), (2, 'LoL Worlds 2024'), (3, 'Esports World Cup 2024');

INSERT INTO tournaments(tournament_id,
						season_id,
                        tournament_name) 
VALUES (1, 2, 'LCK Summer 2024'), (2, 2, 'LCK Worlds Qualifier 2024'), (3, 1, 'LCK Summer 2024');

-- Query the table using left join
SELECT
	s.season_id AS season_id,
    season_name,
    tournament_id,
    tournament_name
FROM seasons AS s
LEFT JOIN tournaments AS t
	USING(season_id);
    

    
    








                                


