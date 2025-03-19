-- Question: Show the provinces that has more patients identified as 'M' than 'F'. Must only show full province_name
-- Category: Hard

WITH
    number_of_patient_per_gender_provinces AS (
SELECT
    province_names.province_name,
    SUM(CASE WHEN patients.gender = 'M' THEN 1 ELSE 0 END) AS male_gender_count,
    SUM(CASE WHEN patients.gender = 'F' THEN 1 ELSE 0 END) AS female_gender_count
FROM
    patients
INNER JOIN
    province_names
ON
    patients.province_id = province_names.province_id
GROUP BY
    province_names.province_name)

SELECT
    province_name
FROM
    number_of_patient_per_gender_provinces
WHERE
    male_gender_count > female_gender_count;

