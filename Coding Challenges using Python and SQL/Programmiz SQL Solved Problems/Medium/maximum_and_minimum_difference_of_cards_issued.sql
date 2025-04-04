-- Question: Write an SQL query to find the difference between price of cards issued
-- Categories: Medium

SELECT
    card_name,
    MAX(issued_amount) - MIN(issued_amount) AS difference
FROM
    Cards
GROUP BY
    card_name
ORDER BY
    difference DESC;

