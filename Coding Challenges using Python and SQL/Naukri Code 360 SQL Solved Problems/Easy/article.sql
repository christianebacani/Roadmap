-- Question: Article
-- Categories: Easy

WITH
    number_of_article_views AS (
SELECT
    viewer_id,
    view_date,
    COUNT(DISTINCT article_id) AS article_count
FROM
    Views
GROUP BY
    viewer_id,
    view_date
    )

SELECT
    viewer_id AS id
FROM
    number_of_article_views
WHERE
    number_of_article_views.article_count > 1
ORDER BY
    id;

