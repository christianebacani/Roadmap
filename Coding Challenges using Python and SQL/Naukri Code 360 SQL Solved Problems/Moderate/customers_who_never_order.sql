-- Question: Customers Who Never Order
-- Categories: Moderate

SELECT
    NameCust AS "Customers"
FROM
    Customers
WHERE
    Id NOT IN (SELECT CustomerId FROM Orders);
