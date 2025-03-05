-- 8 Kyu: Opposites Attract

SELECT
  flower1,
  flower2,
  CASE
    WHEN (flower1 % 2 != 0 AND flower2 % 2 = 0) OR (flower1 % 2 = 0 AND flower2 % 2 != 0) THEN True
    ELSE False
  END AS res
FROM
  love;
