-- Question: Show first name and last name of patients who does not have allergies. (null)
-- Category: Easy

SELECT
    first_name,
    last_name
FROM
    patients
WHERE
    allergies IS NULL;
   
