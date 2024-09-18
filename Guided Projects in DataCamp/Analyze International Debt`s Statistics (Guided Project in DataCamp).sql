-- Use any database 
USE countries;

-- Number of distinct countries present in database
SELECT
	COUNT(DISTINCT country_name) AS total_distinct_countries
FROM international_debt;

-- Query the highest total amount of debt per country
SELECT
	country_name,
    SUM(debt) AS total_debt
FROM international_debt 
GROUP BY country_name
ORDER BY total_debt DESC
LIMIT 1;

-- Country with lowest amount of principal repayments (indicated by the "DT.AMT.DLXF.CD" indicator code)
SELECT
	country_name,
    indicator_name,
	MIN(debt) AS lowest_repayment
FROM international_debt
WHERE indicator_code = 'DT.AMT.DLXF.CD'
GROUP by country_name, indicator_name
ORDER BY lowest_repayment
LIMIT 1;



                        
