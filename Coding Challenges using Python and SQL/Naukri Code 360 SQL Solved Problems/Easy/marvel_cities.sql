-- Question: Marvel Cities
-- Categories: Easy

SELECT *
FROM
    CITY
WHERE
    CountryCode = 'Marv' AND
    Population > 100000;
