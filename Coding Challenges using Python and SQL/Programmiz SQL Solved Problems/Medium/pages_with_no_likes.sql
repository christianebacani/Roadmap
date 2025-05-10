-- Question: Write an SQL query to find pages that received no likes
-- Categories: Medium

SELECT
    page_name,
    course_name
FROM
    Pages
WHERE
    page_id NOT IN (SELECT DISTINCT Likes.page_id FROM Likes WHERE Likes.page_id = Pages.page_id);