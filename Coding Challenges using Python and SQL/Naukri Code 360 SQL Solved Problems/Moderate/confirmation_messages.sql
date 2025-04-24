-- Question: Confirmation of Signups
-- Categories: Moderate

WITH
    user_id_and_num_of_msgs AS (
SELECT
    Signups.user_id,
    SUM(CASE WHEN Confirmations.action_value = 'confirmed' THEN 1 ELSE 0 END) AS total_num_of_confirmed_msgs,
    COUNT(*) AS total_num_of_msgs
FROM
    Signups
LEFT JOIN
    Confirmations
ON
    Signups.user_id = Confirmations.user_id
GROUP BY
    Signups.user_id)

SELECT
    user_id,
    ROUND(total_num_of_confirmed_msgs / (total_num_of_msgs * 1.00), 2) AS confirmation_rate
FROM
    user_id_and_num_of_msgs;

