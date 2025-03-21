-- Questions: Show the city, company_name, contact_name of all customers from cities which contains the letter 'L' in the city name, sorted by contact_name
-- Categories: Easy

SELECT
    city,
    company_name,
    contact_name
FROM
    customers
WHERE
    city LIKE '%L%'
ORDER BY
    contact_name;
