-- Question: Show all patient's first_name, last_name, and birth_date who were born in the 1970s decade. Sort the list starting from the earliest birth_date.
-- Category: Medium

SELECT
    first_name,
    last_name,
    birth_date
FROM
    patients
WHERE
    YEAR(birth_date) BETWEEN 1970 AND 1979
ORDER BY
    birth_date;
