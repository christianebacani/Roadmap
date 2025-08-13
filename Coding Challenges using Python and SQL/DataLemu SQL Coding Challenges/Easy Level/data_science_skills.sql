-- Question: Data Science Skills
-- Category: Linkedin SQL Interview Question

SELECT
  candidate_with_postgresql_skills.candidate_id
FROM (
SELECT
  DISTINCT
  candidate_id
FROM
  candidates
WHERE
  skill = 'Python'
) AS candidate_with_python_skills
INNER JOIN (
SELECT
  DISTINCT
  candidate_id
FROM
  candidates
WHERE
  skill = 'Tableau'
) AS candidate_with_tableau_skills
ON
  candidate_with_python_skills.candidate_id = candidate_with_tableau_skills.candidate_id
INNER JOIN (
SELECT
  DISTINCT
  candidate_id
FROM
  candidates
WHERE
  skill = 'PostgreSQL'
) AS candidate_with_postgresql_skills
ON
  candidate_with_tableau_skills.candidate_id = candidate_with_postgresql_skills.candidate_id