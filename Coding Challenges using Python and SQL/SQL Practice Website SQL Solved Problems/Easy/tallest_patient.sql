-- Question: Show the first_name, last_name, and height of the patient with the greatest height.
-- Category: Easy

SELECT
	first_name,
    last_name,
    height
FROM
	patients
order by
	height DESC
LIMIT
	1;
   