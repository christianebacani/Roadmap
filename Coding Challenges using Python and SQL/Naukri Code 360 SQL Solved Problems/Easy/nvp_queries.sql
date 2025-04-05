-- Question: NVP Queries
-- Categories: Easy

SELECT
    id,
    year,
    COALESCE((SELECT NPV.npv FROM NPV WHERE NPV.id = Queries.id AND NPV.year = Queries.year), 0) AS npv
FROM
    Queries;
