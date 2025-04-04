-- Question: Write an SQL query to retrieve the product names that do not contain any vowels
-- Categories: Medium

SELECT
    product_name
FROM
    Products
WHERE
    (product_name NOT LIKE '%a%' OR product_name NOT LIKE '%A%') AND
    (product_name NOT LIKE '%e%' OR product_name NOT LIKE '%E%') AND
    (product_name NOT LIKE '%i%' OR product_name NOT LIKE '%I%') AND
    (product_name NOT LIKE '%o%' OR product_name NOT LIKE '%O%') AND
    (product_name NOT LIKE '%u%' OR product_name NOT LIKE '%U%');
