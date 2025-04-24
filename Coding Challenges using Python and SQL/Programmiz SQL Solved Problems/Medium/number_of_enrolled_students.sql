-- Question: Write an SQL query to return the number of students enrolled in each subject
-- Categories: Medium

SELECT
    subject,
    COUNT(student_name) AS student_count
FROM
    Enrollment
GROUP BY
    subject
ORDER BY
    student_count;
