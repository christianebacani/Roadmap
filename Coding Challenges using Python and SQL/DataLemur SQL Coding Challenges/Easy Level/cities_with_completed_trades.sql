-- Question: Cities With Completed Trades
-- Categories: Robinhood SQL Interview Question

SELECT
  users.city,
  COUNT(order_id) AS total_orders
FROM
  users
INNER JOIN
  trades
ON
  users.user_id = trades.user_id
WHERE
  trades.status = 'Completed'
GROUP BY
  users.city
ORDER BY
  total_orders DESC
LIMIT
  3;