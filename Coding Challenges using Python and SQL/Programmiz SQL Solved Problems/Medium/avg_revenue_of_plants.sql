-- Question: Write an SQL query to find the average revenue of plants
-- Categories: Medium

SELECT
    plant_name,
    ROUND(AVG(revenue), 2) AS average_revenue
FROM
    Plants
GROUP BY
    plant_name
HAVING
    AVG(revenue) > 40;