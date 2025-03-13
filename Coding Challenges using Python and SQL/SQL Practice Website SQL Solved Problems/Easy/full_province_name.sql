-- Question: Show first name, last name, and the full province name of each patient.
-- Category: Easy

SELECT
	first_name,
    last_name,
    province_names.province_name
FROM
	patients
INNER JOIN
	province_names
ON
	patients.province_id = province_names.province_id;