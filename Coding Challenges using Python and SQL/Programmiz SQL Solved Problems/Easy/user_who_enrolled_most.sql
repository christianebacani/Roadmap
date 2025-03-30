-- Questions: Write an SQL query to find the user who has enrolled in the most courses
-- Categories: Easy

SELECT
    Courses.user_id,
    COUNT(Courses.course_completed) AS course_count
FROM
    Courses
GROUP BY
    Courses.user_id
ORDER BY
    course_count DESC
LIMIT
    1;