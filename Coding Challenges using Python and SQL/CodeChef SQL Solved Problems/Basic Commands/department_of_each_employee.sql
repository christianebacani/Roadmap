-- Basic Commands: Department of Each Employee

SELECT
    department,
    COUNT(employee_id) AS total_employees
FROM
    Employees
GROUP BY
    department;

