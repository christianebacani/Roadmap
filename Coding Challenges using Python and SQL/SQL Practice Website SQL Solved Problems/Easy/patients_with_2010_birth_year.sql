-- Question: Show how many patients have a birth_date with 2010 as the birth year.
-- Categories: Easy

SELECT
    COUNT(patient_id) AS total_patients
FROM
    patients
WHERE
    SUBSTR(birth_date, 1, 4) = '2010';
