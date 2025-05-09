-- Question: Write an SQL query to alter the table according to the instructions
-- Categories: Expert

WITH
    support_tickets_with_urgency_levels AS (
SELECT
    ticket_id,
    ticket_date,
    ticket_status,
    CASE
        WHEN description LIKE '%locked%' OR description LIKE '%connectivity%' THEN 'High'
        WHEN description LIKE '%error%' OR description LIKE '%issues%' THEN 'Medium'
        ELSE 'Low'
    END AS urgency_level
FROM
    SupportTickets
    )


SELECT *
FROM
    support_tickets_with_urgency_levels
WHERE
    urgency_level = 'High'
UNION ALL
SELECT *
FROM
    support_tickets_with_urgency_levels
WHERE
    urgency_level = 'Medium'
UNION ALL
SELECT *
FROM
    support_tickets_with_urgency_levels
WHERE
    urgency_level = 'Low';