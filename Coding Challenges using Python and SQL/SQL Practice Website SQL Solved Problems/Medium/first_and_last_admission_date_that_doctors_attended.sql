-- Question: For each doctor, display their id, full name, and the first and last admission date they attended.
-- Category: Medium

SELECT
    doctors.doctor_id,
    CONCAT(doctors.first_name, ' ', doctors.last_name) AS full_name,
    MIN(admissions.admission_date) AS first_admission_date,
    MAX(admissions.admission_date) AS last_admission_date
FROM
    doctors
INNER JOIN
    admissions
ON
    doctors.doctor_id = admissions.attending_doctor_id
GROUP BY
    doctors.doctor_id,
    CONCAT(doctors.first_name, ' ', doctors.last_name)
