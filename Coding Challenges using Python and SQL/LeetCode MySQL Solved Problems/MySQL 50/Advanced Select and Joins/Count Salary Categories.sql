-- 1907. Count Salary Categories
-- Categories : Database

WITH
    salary_counts AS (
SELECT
    SUM(CASE WHEN income < 20000 THEN 1 ELSE 0 END) AS total_low_salary_count,
    SUM(CASE WHEN income >= 20000 AND income <= 50000 THEN 1 ELSE 0 END) AS total_average_salary_count,
    SUM(CASE WHEN income > 50000 THEN 1 ELSE 0 END) AS total_high_salary_count
FROM
    Accounts)

SELECT
    'Low Salary' AS category,
    total_low_salary_count AS accounts_count
FROM
    salary_counts
UNION ALL
SELECT
    'Average Salary',
    total_average_salary_count
FROM
    salary_counts
UNION ALL
SELECT
    'High Salary',
    total_high_salary_count
FROM
    salary_counts;

    

