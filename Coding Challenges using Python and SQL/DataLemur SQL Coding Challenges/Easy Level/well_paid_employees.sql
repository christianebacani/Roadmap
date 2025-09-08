-- Question: Well Paid Employees
-- Categories: FAANG SQL Interview Question

WITH
  employee_and_manager_salaries AS (
SELECT
  employee_id,
  name AS employee_name,
  salary AS employee_salary,
  manager_id,
  (SELECT inner_employee.salary FROM employee AS inner_employee WHERE inner_employee.employee_id = employee.manager_id) AS manager_salary
FROM
  employee
  )

SELECT
  employee_id,
  employee_name
FROM
  employee_and_manager_salaries
WHERE
  employee_salary > manager_salary;