-- 1934. Confirmation Rate
-- Category : Database

SELECT
    DISTINCT
        user_id,
        ROUND(COALESCE((SELECT
                            COUNT(action)
                        FROM
                            Confirmations AS inner_table
                        WHERE
                            inner_table.user_id = Signups.user_id AND
                            inner_table.action = 'confirmed') /
                        (SELECT
                            COUNT(action)
                        FROM
                            Confirmations AS inner_table
                        WHERE
                            inner_table.user_id = Signups.user_id), 0.00), 2) AS confirmation_rate
FROM
    Signups;
