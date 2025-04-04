-- Question: Write an SQL query to update the table according to the instructions
-- Categories: Medium

UPDATE
    Orders
SET
    status = 'Processing'
WHERE
    status = 'Pending';

SELECT *
FROM
    Orders;

