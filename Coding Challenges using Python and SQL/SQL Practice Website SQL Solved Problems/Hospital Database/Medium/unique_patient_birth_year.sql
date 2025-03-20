-- Question: Show unique birth years from patients and order them by ascending.
-- Category: Medium

SELECT
    DISTINCT(SUBSTR(birth_date, 1, 4)) AS birth_year
FROM
    patients
ORDER BY
    birth_year;

