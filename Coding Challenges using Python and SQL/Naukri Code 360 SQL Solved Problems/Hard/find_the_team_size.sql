-- Question: Find the Team Size
-- Categories: Hard

SELECT
    employee_id,
    (SELECT COUNT(*) FROM Employee AS Inner_Table WHERE Inner_Table.team_id = Employee.team_id) AS team_size
FROM
    Employee;