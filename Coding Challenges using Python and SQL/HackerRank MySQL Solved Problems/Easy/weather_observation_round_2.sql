-- Weather Observation Round 2
-- Categories: Aggregation

SELECT
    CONCAT(ROUND(SUM(LAT_N), 2), ' ', ROUND(SUM(LONG_W), 2))
FROM
    STATION;
