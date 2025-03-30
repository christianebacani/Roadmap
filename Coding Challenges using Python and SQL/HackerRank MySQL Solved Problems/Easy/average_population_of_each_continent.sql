-- Question: Average Population of Each Continent
-- Categories: Basic Join

SELECT
    COUNTRY.Continent,
    FLOOR(AVG(CITY.POPULATION))
FROM
    COUNTRY
INNER JOIN
    CITY
ON
    COUNTRY.Code = CITY.CountryCode
GROUP BY
    COUNTRY.Continent;
