-- Basic Commands: Locate People

SELECT
    department_name,
    location
FROM
    departments
WHERE
    location LIKE 'S%';
