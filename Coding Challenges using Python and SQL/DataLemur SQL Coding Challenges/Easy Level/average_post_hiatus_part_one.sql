-- Question: Average Post Hiatus (Part 1)
-- Categories: Facebook SQL Interview Question

SELECT
  user_id,
  (SELECT MAX(inner_posts.post_date) FROM posts AS inner_posts WHERE inner_posts.user_id = posts.user_id)::DATE -
  (SELECT MIN(inner_posts.post_date) FROM posts AS inner_posts WHERE inner_posts.user_id = posts.user_id)::DATE
  AS days_between
FROM
  posts
WHERE
  EXTRACT(YEAR FROM post_date) = '2021'
GROUP BY
  user_id
HAVING
  COUNT(*) > 1
ORDER BY
  days_between ASC;