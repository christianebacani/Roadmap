-- Question: Employee Bonus
-- Categories: Moderate

WITH
    employee_and_bonuses AS (
SELECT
    Employee.empId,
    Employee.name,
    Bonus.bonus
FROM
    Employee
LEFT JOIN
    Bonus
ON
    Employee.empId = Bonus.empId
    )

SELECT
    name,
    bonus
FROM
    employee_and_bonuses
WHERE
    bonus < 1000 OR
    bonus IS NULL;