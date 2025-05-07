-- Question: Consecutive Available Seats
-- Categories: Moderate

WITH
    current_and_next_seat AS (
SELECT
    seat_id,
    free,
    LEAD(free, 1, '0') OVER (ORDER BY seat_id) AS is_next_seat_available
FROM
    cinema
    )

SELECT
    seat_id
FROM
    current_and_next_seat
WHERE
    free = '1' AND
    is_next_seat_available = '1';