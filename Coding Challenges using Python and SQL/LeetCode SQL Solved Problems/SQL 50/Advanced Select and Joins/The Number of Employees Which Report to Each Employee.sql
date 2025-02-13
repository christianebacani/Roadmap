-- 1731. The Number of Employees Which Report to Each Employee
-- Categories : Database

SELECT
    employee_id,
    name,
    (SELECT COUNT(*) FROM Employees AS inner_table WHERE inner_table.reports_to = Employees.employee_id) AS reports_count,
    ROUND((SELECT AVG(inner_table.age) FROM Employees AS inner_table WHERE inner_table.reports_to = Employees.employee_id)) AS average_age
FROM
    Employees
WHERE
    employee_id IN (SELECT inner_table.reports_to FROM Employees AS inner_table WHERE inner_table.reports_to = Employees.employee_id)
GROUP BY
    employee_id, name
ORDER BY
    employee_id;

