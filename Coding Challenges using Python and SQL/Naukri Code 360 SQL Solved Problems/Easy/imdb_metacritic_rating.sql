-- Question: IMDb Metacritic Rating
-- Categories: Easy

SELECT
	imdb.title AS title,
	imdb.rating AS rating
FROM
	imdb
INNER JOIN
	earning
ON
	imdb.movie_id = earning.movie_id
WHERE
	imdb.title LIKE '%(2012)%' AND
	imdb.metacritic > 60 AND
    earning.domestic > 100000000;