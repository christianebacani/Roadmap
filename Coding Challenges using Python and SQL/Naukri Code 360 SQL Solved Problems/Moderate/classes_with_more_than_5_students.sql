-- Question: Classes with more than 5 students
-- Categories: Moderate

SELECT
    class
FROM
    courses
GROUP BY
    class
HAVING
    COUNT(*) >= 5;
