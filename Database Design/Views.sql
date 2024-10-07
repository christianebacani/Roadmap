-- Specify the Database
USE practicedb;


-- Implementing Views (Virtual Tables)


-- Main table
SELECT *
FROM top_rated_movies;


-- Top 10 highest popularity scores
CREATE VIEW popularity_scores AS 
SELECT
	genres.genre,
	ROUND(AVG((vote_average + vote_count + popularity) / 3), 2) AS avg_popularity_score
FROM top_rated_movies
INNER JOIN genres
	ON genres.genre_id = top_rated_movies.genre_id
GROUP BY genres.genre
ORDER BY avg_popularity_score DESC
LIMIT 10;


-- Total films per genre
CREATE VIEW total_genres AS 
SELECT
	genres.genre,
	COUNT(*) AS total_count
FROM top_rated_movies
INNER JOIN genres
	USING(genre_id)
GROUP BY genres.genre;


-- Top 5 oldest films
CREATE VIEW oldest_films AS 
SELECT *
FROM top_rated_movies
INNER JOIN dates
	USING(date_id)
ORDER BY release_date
LIMIT 5;
































































































