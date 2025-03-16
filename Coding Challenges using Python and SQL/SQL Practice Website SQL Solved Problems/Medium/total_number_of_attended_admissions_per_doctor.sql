-- Question: Show first_name, last_name, and the total number of admissions attended for each doctor. Every admission has been attended by a doctor.
-- Category: Medium

SELECT
    doctors.first_name,
    doctors.last_name,
    COUNT(admissions.attending_doctor_id) AS admissions_total
FROM
    doctors
INNER JOIN
    admissions
ON
    doctors.doctor_id = admissions.attending_doctor_id
GROUP BY
    doctors.first_name,
    doctors.last_name;


