-- 1211. Queries Quality and Percentage
-- Categories : Database

SELECT
    Queries.query_name,
    ROUND(AVG(Queries.rating / Queries.position), 2) AS quality,
    ROUND((SELECT COUNT(inner_table.query_name) FROM Queries AS inner_table WHERE inner_table.rating <= 2 AND inner_table.query_name = Queries.query_name) / (SELECT COUNT(inner_table.query_name) FROM Queries AS inner_table WHERE inner_table.query_name = Queries.query_name) * 100, 2) AS poor_query_percentage
FROM 
    Queries
GROUP BY
    Queries.query_name;
