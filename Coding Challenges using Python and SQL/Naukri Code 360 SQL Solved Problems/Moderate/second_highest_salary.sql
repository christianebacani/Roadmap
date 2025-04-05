-- Question: Second Highest Salary
-- Categories: Moderate

SELECT
    COALESCE(Salary, NULL) AS salary
FROM
    Employee
ORDER BY
    salary DESC
OFFSET
    1
LIMIT
    1;


