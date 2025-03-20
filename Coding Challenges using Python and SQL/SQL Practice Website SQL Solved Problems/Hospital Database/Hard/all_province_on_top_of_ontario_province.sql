-- Question: Sort the province names in ascending order in such a way that the province 'Ontario' is always on top.
-- Categories: Hard

SELECT
    ontario_province.province_name AS province_name
FROM
(SELECT
    province_name
FROM
    province_names
WHERE
    province_name = 'Ontario'
) AS ontario_province
    UNION ALL
SELECT
    all_provinces_except_ontario.province_name
FROM
(SELECT
    province_name
FROM
    province_names
WHERE
    province_name <> 'Ontario'
ORDER BY
    province_name) AS all_provinces_except_ontario
