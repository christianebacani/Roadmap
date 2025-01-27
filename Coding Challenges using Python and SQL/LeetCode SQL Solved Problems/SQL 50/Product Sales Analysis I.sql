-- 1068. Product Sales Analysis I
-- Category Database

SELECT
    Product.product_name,
    Sales.year,
    Sales.price
FROM
    Sales
INNER JOIN
    Product
ON
    Sales.product_id = Product.product_id;
