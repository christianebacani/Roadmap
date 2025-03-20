-- Question: Show the category_name and description from the categories table sorted by category_name.
-- Categories: Easy

SELECT
    category_name,
    description
FROM
    categories
ORDER BY
    category_name;
