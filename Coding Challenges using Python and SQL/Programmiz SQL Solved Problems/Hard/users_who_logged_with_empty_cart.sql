-- Question: Write an SQL query to find the number of users who have logged in but haven't added products to the cart
-- Categories: Hard

WITH
    user_id_and_added_products AS (
SELECT
    user_id,
    (SELECT COUNT(Inner_Table.user_id) FROM Activities AS Inner_Table WHERE Inner_Table.user_id = Activities.user_id AND Inner_Table.activity_type = 'Add to Cart') AS number_of_added_products
FROM
    Activities
    )

SELECT
    COUNT(DISTINCT user_id) AS logged_user_empty_cart
FROM
    user_id_and_added_products
WHERE
    number_of_added_products = 0;