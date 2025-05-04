-- Question: Write an SQL query to find non-fiction movies that are not boring
-- Categories: Medium

SELECT
    title,
    rating
FROM
    Movies
WHERE
    movie_id % 2 <> 0 AND
    description != 'Boring'
ORDER BY
    rating DESC;
