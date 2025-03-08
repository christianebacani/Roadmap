-- Basic Commands: Article views

SELECT
    author_id,
    author_name,
    publication_name
FROM
    Views
WHERE
    view_count = 0
ORDER BY
    author_id;
