-- Question: Write an SQL query to find all the employees who make more than their manager
-- Categories: Medium

WITH
    employee_and_manager_table AS (
SELECT
    employee_id,
    name,
    salary,
    manager_employee_id,
    (SELECT Inner_Table.name FROM Employees AS Inner_Table WHERE Inner_Table.employee_id = Employees.manager_employee_id) AS manager_name,
    (SELECT Inner_Table.salary FROM Employees AS Inner_Table WHERE Inner_Table.employee_id = Employees.manager_employee_id) AS manager_salary    
FROM
    Employees
    )

SELECT
    name AS employee_name,
    salary,
    manager_name,
    manager_salary
FROM
    employee_and_manager_table
WHERE
    salary > manager_salary;

