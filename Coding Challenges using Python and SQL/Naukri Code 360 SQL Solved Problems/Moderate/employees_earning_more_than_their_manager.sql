-- Question: Employees Earning More Than Their Manager
-- Categories: Moderate

WITH
    employee_with_manager_salary AS (
SELECT
    Id,
    Name,
    Salary,
    (SELECT Inner_Table.Salary FROM Employee AS Inner_Table WHERE Inner_Table.Id = Employee.managerId) AS manager_salary
FROM
    Employee
    )

SELECT
    Name AS Employee
FROM
    employee_with_manager_salary
WHERE
    manager_salary IS NOT NULL AND
    Salary > manager_salary;