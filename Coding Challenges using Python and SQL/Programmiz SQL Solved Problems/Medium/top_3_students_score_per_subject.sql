-- Question: Write an SQL query to list the top 3 students for each subject based on their scores
-- Categories: Medium

WITH
    exam_rankings_per_subject AS (
SELECT
    *,
    RANK() OVER (PARTITION BY subject ORDER BY score DESC) AS exam_rank_per_subject
FROM
    Student_Scores
    )

SELECT
    student_name,
    subject,
    score
FROM
    exam_rankings_per_subject
WHERE
    exam_rank_per_subject < 4;