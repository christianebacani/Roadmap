-- Question: Show the first_name, last_name. hire_date of the most recently hired employee.
-- Categories: Easy

SELECT
    first_name,
    last_name,
    hire_date
FROM
    employees
ORDER BY
    hire_date DESC
LIMIT
    1;
