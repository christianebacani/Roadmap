-- Question: Show patient_id, diagnosis from admissions. Find patients admitted multiple times for the same diagnosis.
-- Category: Medium

SELECT
	DISTINCT
    patients.patient_id,
    admissions.diagnosis
FROM
    patients
INNER JOIN
    admissions
ON
    patients.patient_id = admissions.patient_id
WHERE
    admissions.diagnosis IN (SELECT inner_table.diagnosis FROM admissions AS inner_table WHERE inner_table.patient_id = admissions.patient_id GROUP BY inner_table.diagnosis HAVING COUNT(*) > 1);
