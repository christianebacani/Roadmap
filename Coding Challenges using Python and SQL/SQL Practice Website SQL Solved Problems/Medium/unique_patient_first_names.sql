-- Question: Show unique first names from the patients table which only occurs once in the list. For example, if two or more people are named 'John' in the first_name column then don't include their name in the output list. If only 1 person is named 'Leo' then include them in the output.
-- Category: Medium

WITH
    first_name_counts AS (
SELECT
    first_name,
    COUNT(first_name) AS first_name_count
FROM
    patients
GROUP BY
    first_name
    )

SELECT
    first_name
FROM
    first_name_counts
WHERE
    first_name_count = 1;
