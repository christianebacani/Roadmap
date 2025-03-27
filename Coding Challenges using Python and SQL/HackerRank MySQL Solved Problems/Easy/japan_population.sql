-- Japan Population
-- Categories: Aggregation

SELECT
    SUM(POPULATION) AS TOTAL_POPULATION
FROM
    CITY
WHERE
    COUNTRYCODE = 'JPN';
