-- Non-Materialized Views for OLTP System (Kaggle Dataset)


-- Drop view if exists
DROP VIEW IF EXISTS 
	cheapest_games_per_platforms;
DROP VIEW IF EXISTS 
	game_descriptions;



-- Cheapest games per platforms
CREATE VIEW
	cheapest_games_per_platforms AS
WITH	
	cheapest_prices_per_platforms AS (
SELECT
    kaggle_db.platforms.`Platform`,
    MIN(kaggle_db.video_game_reviews.`Price`) AS price
FROM 
	kaggle_db.video_game_reviews
INNER JOIN 
	kaggle_db.platforms
USING(platform_id) 
GROUP BY 
	kaggle_db.platforms.`Platform`
ORDER BY 
	price
)

SELECT
    `Game Title`,
    cheapest_prices_per_platforms.`Platform`,
    cheapest_prices_per_platforms.price
FROM 
	cheapest_prices_per_platforms
INNER JOIN 
	kaggle_db.video_game_reviews
ON 
	cheapest_prices_per_platforms.price = kaggle_db.video_game_reviews.`Price`
ORDER BY 
	cheapest_prices_per_platforms.price;
    

-- Game Descriptions
CREATE VIEW
	game_descriptions AS
SELECT 
    `Game Title`,
    `User Rating`, 
    `Price`, 
    `Platform`,
    `Release Year`,
    `Genre`,
    `User Review Text`,
    `Game Mode`
FROM 
	kaggle_db.video_game_reviews
INNER JOIN 
	kaggle_db.platforms
USING(platform_id)
INNER JOIN 
	kaggle_db.release_years
USING(release_year_id)
INNER JOIN 
	kaggle_db.genres
USING(genre_id)
INNER JOIN
	kaggle_db.game_modes
USING(game_mode_id)
ORDER BY 
	`User Rating` DESC;



-- Creating roles and privileges for OLTP System (Kaggle Dataset)


-- Drop role/s or user accounts if exists
DROP ROLE IF EXISTS 
	users;
DROP USER IF EXISTS 
	'joe'@'localhost';
DROP ROLE IF EXISTS
	data_scientists;
DROP USER IF EXISTS 
	'willie'@'localhost';
DROP ROLE IF EXISTS 
	data_admins;
DROP USER IF EXISTS 
	'christiane'@'localhost';



-- User/Group Roles
CREATE ROLE 
	users; 
CREATE USER 
	'joe'@'localhost';
CREATE ROLE 
	data_scientists;
CREATE USER 
	'willie'@'localhost';
CREATE ROLE
	data_admins;
CREATE USER 
	'christiane'@'localhost';


-- Grant 'SELECT' Privileges of 'game_descriptions' view for 'users', and 'data_scientists' role
GRANT SELECT 
ON
	game_descriptions
TO
	users, data_scientists;


-- Grant 'SELECT' Privileges of 'cheapest_games_per_platforms' view for 'users', and 'data_scientist' role
GRANT SELECT
ON
	cheapest_games_per_platforms
TO 
	users, data_scientists;


-- Grant 'CREATE, SELECT, UPDATE, DELETE' Privileges of 'video_game_reviews' table from 'kaggle_db' database for 'data_admins' role
GRANT CREATE, SELECT, UPDATE, DELETE 
ON 
	kaggle_db.video_game_reviews 
TO
	data_admins;



-- Grant 'users' role privileges to 'joe' user account
GRANT users
TO 
	'joe'@'localhost';


-- Grant 'data_scientists' role to 'willie' user account
GRANT data_scientists
TO 
	'willie'@'localhost';


-- Grant 'data_admin' role to 'christiane' user account
GRANT data_admins
TO
	'christiane'@'localhost';



-- Show privileges 
SHOW GRANTS FOR 'joe'@'localhost';
SHOW GRANTS FOR 'willie'@'localhost';
SHOW GRANTS FOR 'christiane'@'localhost';
