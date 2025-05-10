-- Question: Risiting Temperature
-- Categories: Hard

WITH
    weather_and_previous_day_weather AS (
SELECT
    *,
    LAG(Temperature, 1, NULL) OVER (ORDER BY recordDate ASC) AS previous_day_temperature
FROM
    Weather
    )


SELECT
    id AS "Id"
FROM
    weather_and_previous_day_weather
WHERE
    Temperature > previous_day_temperature;