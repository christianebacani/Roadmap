-- Question: Write an SQL query to display a personalized greeting
-- Categories: Hard

SELECT
    id,
    name,
    CONCAT('Hi, ', name, '!') AS greeting
FROM
    Names