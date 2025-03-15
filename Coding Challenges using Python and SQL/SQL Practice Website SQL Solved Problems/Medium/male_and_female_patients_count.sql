-- Question: Show the total amount of male patients and the total amount of female patients in the patients table. Display the two results in the same row.
-- Category: Medium

SELECT
    DISTINCT
    (SELECT COUNT(inner_table.patient_id) FROM patients AS inner_table WHERE inner_table.gender = 'M') AS male_count,
    (SELECT COUNT(inner_table.patient_id) FROM patients AS inner_table WHERE inner_table.gender = 'F') AS female_count
FROM
    patients;

