-- 1757. Recyclable and Low Fat Products
-- Category : Database 

SELECT
    product_id
FROM
    Products
WHERE
    low_fats = 'Y' AND
    recyclable = 'Y';
     

