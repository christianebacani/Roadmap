-- 1341. Movie Rating
-- Categories : Database

WITH
    user_with_highest_rates AS (
SELECT
    MovieRating.user_id,
    Users.name,
    COUNT(MovieRating.user_id) AS rate_count
FROM
    MovieRating
INNER JOIN
    Users
ON
    MovieRating.user_id = Users.user_id
GROUP BY
    MovieRating.user_id,
    Users.name
ORDER BY
    rate_count DESC,
    Users.name ASC
LIMIT
    1)


SELECT
    user_with_highest_rates.name AS results
FROM
    user_with_highest_rates
UNION ALL
SELECT
    highest_avg_ratings_2020.title
FROM (
SELECT
    MovieRating.movie_id,
    Movies.title,
    AVG(MovieRating.rating) AS avg_rating
FROM
    MovieRating
INNER JOIN
    Movies
ON
    MovieRating.movie_id = Movies.movie_id
WHERE
    MovieRating.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY
    MovieRating.movie_id,
    Movies.title
ORDER BY
    avg_rating DESC,
    Movies.title ASC
LIMIT
    1) AS highest_avg_ratings_2020