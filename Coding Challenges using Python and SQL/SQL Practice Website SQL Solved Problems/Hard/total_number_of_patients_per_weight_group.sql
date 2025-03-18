-- Question: Show all of the patients grouped into weight groups. Show the total amount of patients in each weight group. Order the list by the weight group decending. For example, if they weight 100 to 109 they are placed in the 100 weight group, 110-119 = 110 weight group, etc.
-- Category: Hard

WITH
    patient_weight_groups AS (
SELECT
    patient_id,
    weight,
    CASE
        WHEN weight BETWEEN 0 AND 9 THEN 0
        WHEN weight BETWEEN 10 AND 19 THEN 10
        WHEN weight BETWEEN 20 AND 29 THEN 20
        WHEN weight BETWEEN 30 AND 39 THEN 30
        WHEN weight BETWEEN 40 AND 49 THEN 40
        WHEN weight BETWEEN 50 AND 59 THEN 50
        WHEN weight BETWEEN 60 AND 69 THEN 60
        WHEN weight BETWEEN 70 AND 79 THEN 70
        WHEN weight BETWEEN 80 AND 89 THEN 80
        WHEN weight BETWEEN 90 AND 99 THEN 90
        WHEN weight BETWEEN 100 AND 109 THEN 100
        WHEN weight BETWEEN 110 AND 119 THEN 110
        WHEN weight BETWEEN 120 AND 129 THEN 120
        WHEN weight BETWEEN 130 AND 139 THEN 130
        WHEN weight BETWEEN 140 AND 149 THEN 140
    END AS weight_group
FROM
    patients)

SELECT
    COUNT(patient_id) AS patients_in_group,
    weight_group
FROM
    patient_weight_groups
GROUP BY
    weight_group
ORDER BY
    weight_group DESC;

