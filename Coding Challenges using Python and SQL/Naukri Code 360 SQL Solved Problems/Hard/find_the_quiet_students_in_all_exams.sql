-- Question: Find the Quiet Students in All Exams
-- Categories: Hard

SELECT
    DISTINCT
    Student.student_id,
    Student.student_name
FROM
    Student
INNER JOIN
    Exam
ON
    Student.student_id = Exam.student_id
WHERE
    Student.student_id NOT IN (
SELECT
    DISTINCT
    student_id
FROM
    Exam
WHERE
    score = (SELECT MAX(Inner_Table.score) FROM Exam AS Inner_Table WHERE Inner_Table.exam_id = Exam.exam_id) OR
    score = (SELECT MIN(Inner_Table.score) FROM Exam AS Inner_Table WHERE Inner_Table.exam_id = Exam.exam_id)
    )