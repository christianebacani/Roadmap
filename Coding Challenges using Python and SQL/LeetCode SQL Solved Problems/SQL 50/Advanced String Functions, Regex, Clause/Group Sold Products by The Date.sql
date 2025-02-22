-- 1484. Group Sold Products by The Date
-- Categories : Database

WITH
    sell_date_and_nums_sold AS (
SELECT
    sell_date,
    (SELECT COUNT(DISTINCT inner_table.product) FROM Activities AS inner_table WHERE inner_table.sell_date = Activities.sell_date) AS num_sold
FROM
    Activities
GROUP BY
    sell_date)


SELECT
    sell_date_and_nums_sold.sell_date,
    sell_date_and_nums_sold.num_sold,
    (SELECT GROUP_CONCAT(DISTINCT inner_table.product ORDER BY inner_table.product ASC SEPARATOR ',') FROM Activities AS inner_table WHERE inner_table.sell_date = sell_date_and_nums_sold.sell_date) AS products
FROM
    sell_date_and_nums_sold
ORDER BY
    sell_date_and_nums_sold.sell_date ASC;
