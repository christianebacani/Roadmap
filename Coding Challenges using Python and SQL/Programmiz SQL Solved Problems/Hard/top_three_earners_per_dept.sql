-- Question: Write an SQL query to find the top three earners for each department
-- Categories: Hard

WITH
    employee_and_salary_rank_per_dept AS (
SELECT
    Employee.name,
    Employee.salary,
    Department.department_name,
    ROW_NUMBER() OVER (PARTITION BY Department.department_name ORDER BY Employee.salary DESC, Employee.name ASC) AS salary_rank_per_dept
FROM
    Employee
INNER JOIN
    Department
ON
    Employee.department_id = Department.department_id
    )

SELECT
    department_name,
    name,
    salary
FROM
    employee_and_salary_rank_per_dept
WHERE
    salary_rank_per_dept BETWEEN 1 AND 3;