-- Population Density Difference
-- Categories: Aggregation

SELECT
    MAX(POPULATION) - MIN(POPULATION) AS DIFFERENCE
FROM
    CITY;
