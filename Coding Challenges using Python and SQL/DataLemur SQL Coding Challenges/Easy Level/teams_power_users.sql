-- Question: Teams Power Users
-- Categories: Microsoft SQL Interview Question

SELECT 
  sender_id,
  COUNT(message_id) AS message_count
FROM
  messages
WHERE
  EXTRACT(YEAR FROM sent_date) = '2022' AND
  EXTRACT(MONTH FROM sent_date) = '08'
GROUP BY
  sender_id
ORDER BY
  message_count DESC
LIMIT
  2;