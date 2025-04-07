-- Question: Write an SQL query to find the art pieces renovated in the psat five years
-- Categories: Medium

SELECT
    art_name,
    artist
FROM
    Art
WHERE
    last_renovation BETWEEN '2019-01-01' AND '2024-01-01';
