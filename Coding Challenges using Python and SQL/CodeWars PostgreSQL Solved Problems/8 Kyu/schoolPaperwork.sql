-- 8 Kyu: Beginner Series #1 School Paperwork

SELECT
  n,
  m,
  CASE
    WHEN n <= 0 OR m <= 0 THEN 0
    ELSE n * m
  END AS res
FROM
  paperwork;
  