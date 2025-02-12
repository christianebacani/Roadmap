-- 596. Classes More than 5 Students
-- Categories : Database

SELECT
    class
FROM
    Courses
GROUP BY
    class
HAVING
    COUNT(DISTINCT student) >= 5;
