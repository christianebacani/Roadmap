-- Question: Number of Comments per Post
-- Categories: Moderate

SELECT
    DISTINCT
    sub_id AS post_id,
    (SELECT COUNT(DISTINCT Inner_Table.sub_id) FROM Submissions AS Inner_Table WHERE Inner_Table.parent_id = Submissions.sub_id) AS number_of_comments
FROM
    Submissions
WHERE
    parent_id IS NULL
ORDER BY
    post_id ASC;