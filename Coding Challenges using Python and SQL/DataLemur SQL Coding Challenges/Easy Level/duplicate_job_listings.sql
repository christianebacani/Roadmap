-- Question: Duplicate Job Listings
-- Categories: LinkedIn SQL Interview Question

WITH
  number_of_companies_and_title_with_desc AS (
SELECT
  company_id,
  title,
  description,
  COUNT(*) AS count
FROM
  job_listings
GROUP BY
  company_id,
  title,
  description
  )

SELECT 
  COUNT(company_id) AS duplicate_companies
FROM
  number_of_companies_and_title_with_desc
WHERE
  count = 2;