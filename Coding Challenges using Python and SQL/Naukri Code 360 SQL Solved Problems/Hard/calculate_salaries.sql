-- Question: Calculate Salaries
-- Categories: Hard

WITH
    percentages_of_tax AS (
SELECT
    *,
    CASE
        WHEN max_salary_from_the_company < 1000 THEN 0.0
        WHEN max_salary_from_the_company >= 1000 AND max_salary_from_the_company <= 10000 THEN 24.0
        ELSE 49.0
    END AS percentage
FROM (
SELECT
    *,
    (SELECT MAX(Inner_Table.salary) FROM Salaries AS Inner_Table WHERE Inner_Table.company_id = Salaries.company_id) AS max_salary_from_the_company
FROM
    Salaries
) AS subquery
    )


SELECT
    company_id,
    employee_id,
    employee_name,
    ROUND((salary * 1.0) - ((salary * 1.0) * (percentage / 100.0))) AS salary
FROM
    percentages_of_tax;