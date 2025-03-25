-- 3.) Top 5 shortest movies
-- Categories: Easy
SELECT
    title
FROM
    film
ORDER BY
    length
LIMIT
    5;
