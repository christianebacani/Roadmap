-- Question: Apples & Oranges
-- Categories: Moderate

WITH
    sale_date_and_num_of_apples_and_oranges_sold AS (
SELECT
    DISTINCT
    sale_date,
    (SELECT Inner_Table.sold_num FROM Sales AS Inner_Table WHERE Inner_Table.sale_date = Sales.sale_date AND Inner_Table.fruit = 'apples') AS num_of_apples_sold,
    (SELECT Inner_Table.sold_num FROM Sales AS Inner_Table WHERE Inner_Table.sale_date = Sales.sale_date AND Inner_Table.fruit = 'oranges') AS num_of_oranges_sold
FROM
    Sales
    )

SELECT
    sale_date,
    num_of_apples_sold - num_of_oranges_sold AS diff
FROM
    sale_date_and_num_of_apples_and_oranges_sold
ORDER BY
    sale_date;