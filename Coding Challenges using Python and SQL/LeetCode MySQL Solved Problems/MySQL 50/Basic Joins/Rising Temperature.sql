-- 197. Rising Temperature
-- Category : Database

SELECT
    id
FROM
    Weather
WHERE
    temperature >
    (SELECT temperature
    FROM
        Weather AS inner_table
    WHERE   
        DATEDIFF(Weather.recordDate, inner_table.recordDate) = 1);
    
