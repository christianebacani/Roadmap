-- Question: Write an SQL query to create a truth table for given conditions
-- Categories: Expert

WITH
    operand_and_operations AS (
SELECT
    left_operand,
    (SELECT Operands.value FROM Operands WHERE Operands.name = Operation.left_operand) AS left_operand_value,
    operator,
    right_operand,
    (SELECT Operands.value FROM Operands WHERE Operands.name = Operation.right_operand) AS right_operand_value
FROM
    Operation
    )

SELECT
    left_operand,
    operator,
    right_operand,
    CASE
        WHEN operator = '<' AND left_operand_value < right_operand_value THEN 'TRUE'
        WHEN operator = '>' AND left_operand_value > right_operand_value THEN 'TRUE'
        WHEN operator = '=' AND left_operand_value = right_operand_value THEN 'TRUE'
        ELSE 'FALSE'
    END AS result
FROM
    operand_and_operations;