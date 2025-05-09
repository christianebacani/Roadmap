-- Question: Write an SQL query to identify customers with potential churn risk
-- Categories: Expert

WITH
    customer_and_number_of_transacts AS (
SELECT
    DISTINCT
    Customers.customer_id,
    Customers.customer_name,
    (SELECT COUNT(DISTINCT Inner_Table.transaction_id) FROM Transactions AS Inner_Table WHERE Inner_Table.customer_id = Customers.customer_id) AS number_of_transactions,
    (SELECT Inner_Table.transaction_date FROM Transactions AS Inner_Table WHERE Inner_Table.customer_id = Customers.customer_id ORDER BY Inner_Table.transaction_date DESC LIMIT 1) AS latest_transaction_date
FROM
    Customers
INNER JOIN
    Transactions
ON
    Customers.customer_id = Transactions.customer_id
    )

SELECT
    customer_id,
    customer_name,
    latest_transaction_date AS last_purchase_date,
    number_of_transactions AS total_purchases
FROM
    customer_and_number_of_transacts
WHERE
    number_of_transactions > 2;