-- 1148. Article Views I
-- Category : Database

SELECT
    DISTINCT author_id AS id
FROM
    Views
WHERE
    author_id = viewer_id
ORDER BY
    id;
