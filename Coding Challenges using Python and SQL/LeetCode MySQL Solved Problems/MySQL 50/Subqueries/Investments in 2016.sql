-- 585. Investments in 2016
-- Categories : Database

SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM
    Insurance
WHERE
    tiv_2015 IN (SELECT inner_table.tiv_2015 FROM Insurance AS inner_table WHERE inner_table.pid <> Insurance.pid) AND
    CONCAT(lat, ', ', lon) NOT IN (SELECT CONCAT(inner_table.lat, ', ', inner_table.lon) FROM Insurance AS inner_table WHERE inner_table.pid <> Insurance.pid);
