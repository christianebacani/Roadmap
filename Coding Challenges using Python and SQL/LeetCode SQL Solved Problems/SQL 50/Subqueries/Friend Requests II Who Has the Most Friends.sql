-- 602. Friend Requests II: Who Has the Most Friends
-- Categories : Database

SELECT
    id,
    num
FROM
(SELECT
    requester_id AS id,
    (SELECT COALESCE(COUNT(inner_table.accepter_id), 0) FROM RequestAccepted AS inner_table WHERE inner_table.requester_id = RequestAccepted.requester_id) +
    (SELECT COALESCE(COUNT(inner_table.requester_id), 0) FROM RequestAccepted AS inner_table WHERE inner_table.accepter_id = RequestAccepted.requester_id) AS num
FROM
    RequestAccepted
GROUP BY
    requester_id
UNION ALL
SELECT
    accepter_id AS id,
    (SELECT COALESCE(COUNT(inner_table.requester_id), 0) FROM RequestAccepted AS inner_table WHERE inner_table.accepter_id = RequestAccepted.accepter_id) +
    (SELECT COALESCE(COUNT(inner_table.accepter_id), 0) FROM RequestAccepted AS inner_table WHERE inner_table.requester_id = RequestAccepted.accepter_id) AS num
FROM
    RequestAccepted
GROUP BY
    accepter_id
ORDER BY
    num DESC
LIMIT
    1) AS subquery;


