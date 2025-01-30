-- 1661. Average Time of Process Per Machine
-- Category : Database

SELECT
    DISTINCT main_table.machine_id,
    ROUND(((SELECT
                SUM(timestamp)
            FROM
                Activity AS first_inner_table
            WHERE
                first_inner_table.machine_id = main_table.machine_id AND
                activity_type = 'end') -
            (SELECT
                SUM(timestamp)
            FROM
                Activity AS second_inner_table
            WHERE
                second_inner_table.machine_id = main_table.machine_id AND
                activity_type = 'start')) / 
            (SELECT
                COUNT(DISTINCT process_id)
            FROM
                Activity AS third_inner_table
            WHERE
                third_inner_table.machine_id = main_table.machine_id), 3) AS processing_time
FROM
    Activity AS main_table;