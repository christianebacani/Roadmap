-- Question: African Cities
-- Categories: Basic Join

SELECT
    CITY.NAME
FROM
    COUNTRY
INNER JOIN
    CITY
ON
    COUNTRY.CODE = CITY.COUNTRYCODE
WHERE
    COUNTRY.CONTINENT = 'Africa';
