-- Question: Write an SQL query to convert each name in title case
-- Categories: Hard

SELECT
    user_id,
    CONCAT(UPPER(SUBSTRING(name, 1, 1)), '', LOWER(SUBSTRING(name, 2, LENGTH(name) - 1))) AS name
FROM
    Users;