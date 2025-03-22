-- Question: Show the category_name and the average product unit price for each category rounded to 2 decimal places.
-- Categories: Medium

SELECT
    categories.category_name,
    ROUND(AVG(unit_price), 2) AS average_unit_price
FROM
    categories
INNER JOIN
    products
ON
    categories.category_id = products.category_id
GROUP BY
    categories.category_name;
