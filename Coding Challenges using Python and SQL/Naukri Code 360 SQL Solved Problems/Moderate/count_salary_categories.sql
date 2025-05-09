-- Question: Count Salary Categories
-- Categories: Moderate

SELECT
    'Low Salary' AS category,
    COUNT(*) AS accounts_count
FROM
    Accounts
WHERE
    income < 20000
UNION ALL
SELECT
    'Average Salary' AS category,
    COUNT(*) AS accounts_count
FROM
    Accounts
WHERE
    income >= 20000 AND income <= 50000
UNION ALL 
SELECT
    'High Salary' AS category,
    COUNT(*)
FROM
    Accounts
WHERE
    income > 50000;