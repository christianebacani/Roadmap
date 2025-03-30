-- Question: Write an SQL query to find all dates that were hotter than the previous day
-- Categories: Medium

WITH
    current_and_previous_day_temp AS (
SELECT
    Temperature.record_date,
    Temperature.temperature,
    LAG(Temperature.temperature, 1, NULL) OVER(ORDER BY Temperature.record_date ASC) AS previous_day_temperature
FROM
    Temperature
    )


SELECT
    current_and_previous_day_temp.record_date,
    current_and_previous_day_temp.temperature
FROM
    current_and_previous_day_temp
WHERE
    current_and_previous_day_temp.temperature > current_and_previous_day_temp.previous_day_temperature