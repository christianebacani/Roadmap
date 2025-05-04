-- Question: Write an SQL query to display the new id and name of the students
-- Categories: Hard

SELECT
    CASE
        WHEN id % 2 <> 0 THEN LEAD(id, 1, id) OVER (ORDER BY id)
        ELSE LAG(id, 1, id) OVER (ORDER BY id)
    END AS id,
    name
FROM
    Students
ORDER BY
    id;
