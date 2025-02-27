-- 175.) Combine Two Tables
-- Category Name : Dataase

SELECT
    Person.firstName,
    Person.lastName,
    COALESCE(Address.city) AS city, 
    COALESCE(Address.state) AS state
FROM
    Person
LEFT JOIN
    Address
USING(personId);
