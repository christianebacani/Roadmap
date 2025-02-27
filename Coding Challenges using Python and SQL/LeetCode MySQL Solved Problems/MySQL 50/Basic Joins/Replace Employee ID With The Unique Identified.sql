-- 1378. Replace Employee ID With The Unique Identified
-- Category : Database

SELECT
    unique_id,
    name
FROM
    EmployeeUni
RIGHT JOIN
    Employees
ON
    EmployeeUni.id = Employees.id;
