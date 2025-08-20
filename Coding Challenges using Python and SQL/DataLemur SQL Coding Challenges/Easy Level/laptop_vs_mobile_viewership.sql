-- Question: Laptop vs. Mobile Vieweship
-- Categories: NY Times SQL Interview Question

WITH
  laptop_viewerships AS (
  SELECT
    COUNT(*) AS laptop_views
  FROM
    viewership
  WHERE
    device_type = 'laptop'
  ),
  mobile_viewerships AS (
  SELECT
    COUNT(*) AS mobile_views
  FROM
    viewership
  WHERE
    device_type IN ('tablet', 'phone')
  )

SELECT
  (SELECT * FROM laptop_viewerships) AS laptop_views,
  (SELECT * FROM mobile_viewerships) AS mobile_views