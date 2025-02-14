-- 1789. Primary Department for Each Employee
-- Categories : Database

SELECT
    DISTINCT employee_id,
    COALESCE((SELECT inner_table.department_id FROM Employee AS inner_table WHERE inner_table.employee_id = Employee.employee_id AND inner_table.primary_flag = 'Y'), department_id) AS department_id
FROM
    Employee;

