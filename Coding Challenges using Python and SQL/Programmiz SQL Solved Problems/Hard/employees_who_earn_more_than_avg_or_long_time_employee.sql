-- Question: Write an SQL query to find employees who either earn above average or have been employed for a long time
-- Categories: Hard

SELECT *
FROM
    Employees
WHERE
    years_employed > 10
UNION
SELECT *
FROM
    Employees
WHERE
    salary > (SELECT AVG(Inner_Table.salary) FROM Employees AS Inner_Table WHERE Inner_Table.department = Employees.department);
