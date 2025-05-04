-- Question: Write an SQL query to retrieve the information of each salesperson working for ABC company
-- Categories: Hard

SELECT
    Salespersons.first_name,
    Salespersons.last_name,
    COALESCE(Address.city, '') AS city,
    COALESCE(Address.state, '') AS state
FROM
    Salespersons
LEFT JOIN
    Address
ON
    Salespersons.salesperson_id = Address.salesperson_id
