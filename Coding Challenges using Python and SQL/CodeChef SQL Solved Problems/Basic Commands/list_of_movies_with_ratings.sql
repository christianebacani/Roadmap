-- Basic Commands: List of Movies with Ratings

SELECT
    Movie_name
FROM
    Cinema
WHERE
    Rating > 7 AND
    Rating < 9;
