-- 7 Kyu: SQL with LOTR: Elven Wildcards

SELECT
  INITCAP(CONCAT(firstname, ' ', lastname)) AS shortlist
FROM
  Elves
WHERE
  firstname LIKE '%tegil%' OR
  lastname LIKE '%astar%';

