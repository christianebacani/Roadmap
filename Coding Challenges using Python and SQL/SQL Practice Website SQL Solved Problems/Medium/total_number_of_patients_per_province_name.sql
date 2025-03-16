-- Question: Display the total amount of patients for each province. Order by descending.
-- Category: Medium

SELECT
    province_names.province_name,
    COUNT(*) AS patient_count
FROM
    patients
INNER JOIN 
    province_names
ON 
    patients.province_id = province_names.province_id
GROUP BY
    province_names.province_name
ORDER BY
    patient_count DESC;
