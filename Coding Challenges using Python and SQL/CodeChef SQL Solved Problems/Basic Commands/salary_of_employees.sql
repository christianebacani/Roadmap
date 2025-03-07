-- Basic Commands: Salary of Employees

SELECT
    employee_name,
    company,
    salary
FROM
    Employees
WHERE
    category = 'Full-Time'
ORDER BY
    salary DESC;

    