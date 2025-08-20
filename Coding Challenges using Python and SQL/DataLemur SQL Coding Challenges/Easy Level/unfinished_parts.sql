-- Question: Unfinished Parts
-- Categories: Tesla SQL Interview Question

SELECT
  part,
  assembly_step
FROM
  parts_assembly
WHERE
  finish_date IS NULL