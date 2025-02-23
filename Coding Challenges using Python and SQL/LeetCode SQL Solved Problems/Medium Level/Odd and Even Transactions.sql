-- 3220. Odd and Even Transactions
-- Categories : Database

SELECT
    DISTINCT transaction_date,
    (SELECT COALESCE(SUM(transactions_inner_table.amount), 0) FROM transactions AS transactions_inner_table WHERE transactions_inner_table.transaction_date = transactions.transaction_date AND transactions_inner_table.amount % 2 = 1) AS odd_sum,
    (SELECT COALESCE(SUM(transactions_inner_table.amount), 0) FROM transactions AS transactions_inner_table WHERE transactions_inner_table.transaction_date = transactions.transaction_date AND transactions_inner_table.amount % 2 = 0) AS even_sum
FROM
    transactions
ORDER BY
    transaction_date;
