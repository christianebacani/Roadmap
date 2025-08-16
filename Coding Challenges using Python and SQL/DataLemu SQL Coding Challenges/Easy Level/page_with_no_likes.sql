-- Question: Page With No Likes
-- Category: Facebook SQL Interview Question

SELECT
  page_id
FROM
  pages
WHERE
  page_id NOT IN (
  SELECT
    page_id
  FROM
    page_likes
  )
ORDER BY
  page_id;