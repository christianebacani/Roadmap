-- Question: Director's Actor
-- Categories: Easy

SELECT
    coworked_counts.actor_id,
    coworked_counts.director_id
FROM
(SELECT
    ActorDirector.actor_id,
    ActorDirector.director_id,
    COUNT(*) AS coworked_count
FROM
    ActorDirector
GROUP BY
    ActorDirector.actor_id,
    ActorDirector.director_id) AS coworked_counts
WHERE
    coworked_counts.coworked_count = 3;
    