-- Create materialize view/s
CREATE TABLE 
	kaggle_db.average_price_per_game_platforms AS
SELECT 
	`Platform`,
    ROUND(AVG(`Price`), 2) AS `Average Price Per Game Platform`
FROM 
	kaggle_db.video_game_reviews
GROUP BY 
	`Platform`
ORDER BY 
	`Average Price Per Game Platform` DESC;


-- Create another materialize view
CREATE TABLE
	kaggle_db.highest_rating_games_per_release_years AS
WITH 
	highest_ratings_per_release_years AS (
SELECT 
	`Release Year`,
    MAX(`User Rating`) AS `Highest Ratings`
FROM 
	kaggle_db.video_game_reviews
GROUP BY 
	`Release Year`
ORDER BY 
	`Highest Ratings` DESC
)
SELECT
	highest_ratings_per_release_years.`Release Year`,
    highest_ratings_per_release_years.`Highest Ratings`,
    kaggle_db.video_game_reviews.`Game Title`
FROM
	highest_ratings_per_release_years
INNER JOIN 
	kaggle_db.video_game_reviews
ON
	kaggle_db.video_game_reviews.`Release Year` = highest_ratings_per_release_years.`Release Year` AND
    kaggle_db.video_game_reviews.`User Rating` = highest_ratings_per_release_years.`Highest Ratings`
ORDER BY 
	highest_ratings_per_release_years.`Highest Ratings` DESC;



-- Insert Trigger
DELIMITER //
CREATE TRIGGER kaggle_db.trigger_after_insert AFTER INSERT ON kaggle_db.video_game_reviews
FOR EACH ROW
	BEGIN 
		INSERT INTO kaggle_db.average_price_per_game_platforms (`Platform`, `Price`) 
        VALUES (NEW.`Platform`, NEW.`Price`);
        
		INSERT INTO kaggle_db.highest_rating_games_per_release_years (`Release Year`, `User Rating`, `Game Title`)
        VALUES (NEW.`Release Year`, NEW.`User Rating`, NEW.`Game Title`);
    END //
	

-- Update trigger
DELIMITER //
CREATE TRIGGER kaggle_db.trigger_after_update AFTER UPDATE ON kaggle_db.video_game_reviews
FOR EACH ROW
	BEGIN 
		UPDATE kaggle_db.average_price_per_game_platforms
        SET
			`Platform` = NEW.`Platform`,
            `Price` = NEW.`Price`
		WHERE 
			`Game Title` = OLD.`Game Title`;
            
		UPDATE kaggle_db.highest_rating_games_per_release_years
		SET 
			`Release Year` = NEW.`Release Year`,
            `User Rating` = NEW.`User Rating`,
            `Game Title` = NEW.`Game Title`
        WHERE 
			`Game Title` = OLD.`Game Title`;
	END //


-- Delete Trigger
DELIMITER //
CREATE TRIGGER kaggle_db.trigger_after_delete AFTER DELETE ON kaggle_db.video_game_reviews
FOR EACH ROW
	BEGIN
		DELETE FROM kaggle_db.average_price_per_game_platforms 
        WHERE 
			`Game Title` = OLD.`Game Title`;
            
		DELETE FROM kaggle_db.highest_rating_games_per_release_years
        WHERE
			`Game Title` = OLD.`Game Title`;
	END //


-- Create event to refresh materialize view
DELIMITER //
CREATE EVENT kaggle_db.refresh_average_price_per_game_platforms
ON SCHEDULE EVERY 12 HOUR
DO 
	BEGIN
		TRUNCATE TABLE kaggle_db.average_price_per_game_platforms;
        INSERT INTO kaggle_db.average_price_per_game_platforms (`Platform`, `Average Price Per Game Platform`) 
        SELECT 
			`Platform`,
			ROUND(AVG(`Price`), 2)
		FROM 
			kaggle_db.video_game_reviews
		GROUP BY 
			`Platform`
		ORDER BY 
			`Average Price Per Game Platform` DESC;
	END //


-- Create event
DELIMITER //
CREATE EVENT kaggle_db.refresh_highest_rating_games_per_release_years
ON SCHEDULE EVERY 12 HOUR
DO
	BEGIN
		TRUNCATE TABLE kaggle_db.highest_rating_games_per_release_years;
		INSERT INTO 
			kaggle_db.highest_rating_games_per_release_years (`Release Year`, `User Rating`, `Game Title`) 
		WITH 
			highest_ratings_per_release_years AS (
			SELECT 
				`Release Year`,
				MAX(`User Rating`) AS `Highest Ratings`
			FROM 
				kaggle_db.video_game_reviews
			GROUP BY 
				`Release Year`
			ORDER BY 
				`Highest Ratings` DESC)
		SELECT
			highest_ratings_per_release_years.`Release Year`,
			highest_ratings_per_release_years.`Highest Ratings`,
			kaggle_db.video_game_reviews.`Game Title`
		FROM
			highest_ratings_per_release_years
		INNER JOIN 
			kaggle_db.video_game_reviews
		ON
			kaggle_db.video_game_reviews.`Release Year` = highest_ratings_per_release_years.`Release Year` AND
			kaggle_db.video_game_reviews.`User Rating` = highest_ratings_per_release_years.`Highest Ratings`
		ORDER BY 
			highest_ratings_per_release_years.`Highest Ratings` DESC;
	END //
        

-- Create roles
CREATE ROLE
	data_analysts;    
CREATE ROLE
	data_scientists;


-- Grant privilege to data_analysts role
GRANT SELECT
ON 
	kaggle_db.average_price_per_game_platforms
TO 
	data_analysts;


-- Grant privilege to data_scientists role
GRANT SELECT
ON 
	kaggle_db.highest_rating_games_per_release_years
TO 
	data_scientists;


-- Create user 'chris'
CREATE USER 
	'chris'@'localhost';
    

-- Creat user 'cj'
CREATE USER 
	'cj'@'localhost';

    
-- Grant data_analysts role to user 'chris'
GRANT data_analysts
TO 
	'chris'@'localhost';
    

-- Grant data_scientists role to user 'cj'
GRANT data_scientists
TO
	'cj'@'localhost';


-- Show privileges for the user accounts
SHOW GRANTS FOR 'chris'@'localhost';
SHOW GRANTS FOR 'cj'@'localhost';

    
    
    
    
    
    
    
