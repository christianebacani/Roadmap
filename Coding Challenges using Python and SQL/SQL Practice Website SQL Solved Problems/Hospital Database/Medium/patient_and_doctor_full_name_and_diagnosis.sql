-- Question: For every admission, display the patient's full name, their admission diagnosis, and their doctor's full name who diagnosed their problem.
-- Category: Medium

SELECT
    CONCAT(patients.first_name, ' ', patients.last_name) AS patient_name,
    admissions.diagnosis,
    CONCAT(doctors.first_name, ' ', doctors.last_name) AS doctor_name
FROM
    admissions
INNER JOIN
    patients
ON 
    admissions.patient_id = patients.patient_id
INNER JOIN
    doctors
ON
    admissions.attending_doctor_id = doctors.doctor_id;

