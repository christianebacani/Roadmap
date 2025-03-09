-- Question: Show first name of patients that start with the letter 'C'
-- Category: Easy

SELECT
	first_name
 FROM
 	patients
 WHERE
 	first_name LIKE 'C%';