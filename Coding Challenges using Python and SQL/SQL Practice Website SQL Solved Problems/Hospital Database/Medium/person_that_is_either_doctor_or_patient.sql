-- Question: Show first name, last name and role of every person that is either patient or doctor. The roles are either "Patient" or "Doctor"
-- Category: Medium

SELECT
    first_name,
    last_name,
    'Patient' AS role
FROM
    patients
    UNION ALL
SELECT
    first_name,
    last_name,
    'Doctor' AS role
FROM
    doctors;

