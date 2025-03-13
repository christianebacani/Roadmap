-- Question: Show first name and last name concatinated into one column to show their full name.
-- Category: Easy

SELECT
    CONCAT(first_name, ' ', last_name) AS full_name
FROM
    patients;
