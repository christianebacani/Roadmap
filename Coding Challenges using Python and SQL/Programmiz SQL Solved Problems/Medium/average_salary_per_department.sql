-- Question: Write an SQL query to find the average salary in each department
-- Categories: Medium

SELECT
    department,
    AVG(salary) AS avg_salary
FROM
    Employees
GROUP BY
    department;
