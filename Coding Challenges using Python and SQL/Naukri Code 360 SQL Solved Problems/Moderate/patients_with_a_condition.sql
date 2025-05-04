-- Question: Patients With a Condition
-- Categories: Moderate

SELECT *
FROM
    Patients
WHERE
    conditions LIKE '%DIAB1%';
