-- Revising Aggregations - Averages
-- Categories: Aggregation

SELECT
    AVG(POPULATION) AS AVG_POPULATION
FROM
    CITY
WHERE
    DISTRICT = 'California';
