-- Question: Write an SQL query to find the total viewership for a device
-- Categories: Medium

SELECT
    SUM(CASE WHEN device_type = 'Laptop' THEN 1 ELSE 0 END) AS laptop_views,
    SUM(CASE WHEN device_type IN ('Tablet', 'Phone') THEN 1 ELSE 0 END) AS mobile_views
FROM
    Viewership;