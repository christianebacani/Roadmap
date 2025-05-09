-- Question: Write an SQL query to find the day where the temperature is closest to the monhtly average
-- Categories: Expert

WITH
    Temperature_and_Avg_Temp AS (
SELECT
    *,
    (SELECT AVG(Inner_Table.temperature) FROM Temperature AS Inner_Table WHERE Inner_Table.city = Temperature.city AND
    SUBSTRING(CAST(Inner_Table.date AS VARCHAR), 6, 2) = SUBSTRING(CAST(Temperature.date AS VARCHAR), 6, 2)) AS avg_temp_per_city_and_month
FROM
    Temperature
    )

SELECT
    city,
    date,
    temperature
FROM (
SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY city, SUBSTRING(CAST(date AS VARCHAR), 6, 2) ORDER BY difference) AS difference_rank
FROM (
SELECT
    *,
    ROUND(ABS(temperature - avg_temp_per_city_and_month), 2) AS difference
FROM
    Temperature_and_Avg_Temp
    ) AS differences
) AS difference_rankings
WHERE
    difference_rank = 1
ORDER BY
    temperature DESC;