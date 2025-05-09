-- Question: Fix Names in a Table
-- Categories: Moderate

SELECT
    user_id,
    CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2, LENGTH(name) - 1))) AS name
FROM
    Users
ORDER BY
    user_id;