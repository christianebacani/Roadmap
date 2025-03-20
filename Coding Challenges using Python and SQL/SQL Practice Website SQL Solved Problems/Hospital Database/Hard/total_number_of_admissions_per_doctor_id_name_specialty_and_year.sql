-- Question: We need a breakdown for the total amount of admissions each doctor has started each year. Show the doctor_id, doctor_full_name, specialty, year, total_admissions for that year.
-- Categories: Hard

SELECT
    doctors.doctor_id,
    CONCAT(doctors.first_name, ' ', doctors.last_name) AS doctor_name,
    doctors.specialty,
    YEAR(admissions.admission_date) AS selected_year,
    COUNT(*) AS total_admissions
FROM
    admissions
INNER JOIN
    doctors
ON
    admissions.attending_doctor_id = doctors.doctor_id
GROUP BY
    doctors.doctor_id,
    CONCAT(doctors.first_name, ' ', doctors.last_name),
    doctors.specialty,
    YEAR(admissions.admission_date)
