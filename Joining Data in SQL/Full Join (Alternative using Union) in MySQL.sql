-- Use any database 
USE countries;

-- Drop the unnecessary tables
DROP TABLE IF EXISTS korean_players;
DROP TABLE IF EXISTS chinese_players;

-- Implementing Full Join (Alternatively using UNION in MySQL)

-- Creating the table
CREATE TABLE korean_players(player_id INT PRIMARY KEY,
							name VARCHAR(50),
                            total_earnings INT);

CREATE TABLE chinese_players(player_id INT PRIMARY KEY,
								name VARCHAR(50),
                                total_earnings INT);

-- Inserting a value to the table
INSERT INTO korean_players(player_id, name, total_earnings)
VALUES (1, 'T1 Faker', 1200000), (2, 'KT Deft', 533702), (3, 'HLE Peanut', 655283);

INSERT INTO chinese_players(player_id, name, total_earnings) 
VALUES (1, 'RNG Uzi', 550246), (4, 'TES Meiko', 574679), (5, 'FPX Doinb', 397226);


-- Querying the created table with data using UNION(Alternative for FULL JOIN in MySQL)
SELECT 
	k.player_id AS player_id,
    k.name AS korean_player,
    c.name AS chinese_player
FROM korean_players AS k
LEFT JOIN chinese_players AS c
	USING(player_id) 
UNION
SELECT
	c.player_id AS player_id,
    k.name AS korean_player,
    c.name AS chinese_player
FROM korean_players AS k
RIGHT JOIN chinese_players AS c
	USING(player_id);









	




