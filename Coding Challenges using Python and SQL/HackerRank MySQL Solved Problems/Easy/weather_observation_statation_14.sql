-- Weather Observation Station 14
-- Categories: Aggregation

SELECT
    ROUND(MAX(LAT_N), 4) AS MAXIMUM_LAT_N
FROM
    STATION
WHERE
    ROUND(LAT_N, 4) < 137.2345;
