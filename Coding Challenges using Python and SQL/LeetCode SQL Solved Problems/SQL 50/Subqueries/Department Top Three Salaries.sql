-- 185. Department Top Three Salaries
-- Categories : Database

WITH
    top3_highest_salary_per_dept AS (
SELECT
    id,
    name,
    (SELECT DISTINCT inner_table.salary FROM Employee AS inner_table WHERE inner_table.departmentId = Department.id ORDER BY inner_table.salary DESC LIMIT 1) AS first_highest_salary,
    (SELECT DISTINCT inner_table.salary FROM Employee AS inner_table WHERE inner_table.departmentId = Department.id ORDER BY inner_table.salary DESC LIMIT 1 OFFSET 1) AS second_highest_salary,
    (SELECT DISTINCT inner_table.salary FROM Employee AS inner_table WHERE inner_table.departmentId = Department.id ORDER BY inner_table.salary DESC LIMIT 1 OFFSET 2) AS third_highest_salary
FROM
    Department)

SELECT
    top3_highest_salary_per_dept.name AS Department,
    Employee.name AS Employee,
    Employee.salary AS Salary
FROM
    Employee
INNER JOIN
    top3_highest_salary_per_dept
ON
    Employee.departmentId = top3_highest_salary_per_dept.id AND
    (Employee.salary = top3_highest_salary_per_dept.first_highest_salary OR
    Employee.salary = top3_highest_salary_per_dept.second_highest_salary OR
    Employee.salary = top3_highest_salary_per_dept.third_highest_salary);



