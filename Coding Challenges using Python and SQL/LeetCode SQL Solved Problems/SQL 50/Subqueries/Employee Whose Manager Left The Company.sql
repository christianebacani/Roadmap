-- 1978. Employee Whose Manager Left The Company
-- Categories : Database

SELECT
    employee_id
FROM
    Employees
WHERE
    manager_id NOT IN (SELECT employee_id FROM Employees) AND
    manager_id IS NOT NULL AND
    salary < 30000
ORDER BY
    employee_id;



    