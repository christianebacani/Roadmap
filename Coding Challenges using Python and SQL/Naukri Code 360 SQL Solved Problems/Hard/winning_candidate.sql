-- Question: Winning Candidate
-- Categories: Hard

WITH
    voters_and_candidates AS (
SELECT
    Vote.id AS voter_id,
    Candidate.Name AS voter_name,
    Vote.CandidateId AS candidate_id,
    (SELECT Inner_table.Name FROM Candidate AS Inner_Table WHERE Inner_Table.id = Vote.CandidateId) AS candidate_name
FROM
    Candidate
INNER JOIN
    Vote
ON
    Candidate.id = Vote.id
    )

SELECT
    candidate_name AS "Name"
FROM (
SELECT
    candidate_name,
    COUNT(*) AS number_of_votes
FROM
    voters_and_candidates
GROUP BY
    candidate_name
ORDER BY
    number_of_votes DESC
LIMIT
    1
    ) AS candidate_with_highest_votes;