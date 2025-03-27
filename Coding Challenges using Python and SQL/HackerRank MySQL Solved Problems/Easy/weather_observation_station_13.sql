-- Weather Observation Station 13
-- Categories: Aggregation

SELECT
    ROUND(SUM(LAT_N), 4) AS SUM_OF_LAT_N
FROM
    STATION
WHERE
    ROUND(LAT_N, 4) BETWEEN 38.7881 AND 137.2344;

