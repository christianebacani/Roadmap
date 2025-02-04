-- 570. Managers with at Least 5 Direct Reports
-- Category : Database

WITH
    qualified_managers AS (
SELECT
    managerId
FROM
    Employee
GROUP BY
    managerId
HAVING
    COUNT(managerId) >= 5)


SELECT
    name
FROM
    Employee
WHERE
    id IN (SELECT managerId FROM qualified_managers);
