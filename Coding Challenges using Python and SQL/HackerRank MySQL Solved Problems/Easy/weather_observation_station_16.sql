-- Weather Observation Station 16
-- Categories: Aggregation

SELECT
    ROUND(MIN(LAT_N), 4) AS SMALLEST_LAT_N
FROM
    STATION
WHERE
    ROUND(LAT_N, 4) > 38.7880;
