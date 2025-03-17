-- Display a single row with max_visits, min_visits, average_visits where the maximum, minimum and average number of admissions per day is calculated. Average is rounded to 2 decimal places.
-- Category: Medium

WITH
    num_of_visits_per_admission_date AS (
SELECT
    admission_date,
    COUNT(*) AS num_of_visits
FROM
    admissions
GROUP BY
    admission_date
)

SELECT
    MAX(num_of_visits) AS max_visits,
    MIN(num_of_visits) AS min_visits,
    ROUND(AVG(num_of_visits), 2) AS average_visits
FROM
    num_of_visits_per_admission_date
