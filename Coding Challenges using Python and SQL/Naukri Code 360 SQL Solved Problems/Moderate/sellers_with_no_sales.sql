-- Question: Sellers With No Sales
-- Categories: Moderate

WITH
    seller_name_and_num_of_sales_made_in_year_2020 AS (
SELECT
    seller_name,
    (SELECT COUNT(Inner_Table.sale_date) FROM Orders AS Inner_Table WHERE Inner_Table.seller_id = Seller.seller_id AND Inner_Table.sale_date BETWEEN '2020-01-01' AND '2020-12-31') AS number_of_sales_made_in_year_2020
FROM
    Seller
    )

SELECT
    seller_name
FROM
    seller_name_and_num_of_sales_made_in_year_2020
WHERE
    number_of_sales_made_in_year_2020 = 0
ORDER BY
    seller_name;