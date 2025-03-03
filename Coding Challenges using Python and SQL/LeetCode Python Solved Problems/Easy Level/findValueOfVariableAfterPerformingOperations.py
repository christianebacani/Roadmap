# 2011. Final Value of Variable after Performing operations
# Categories : Array, String, Simulation

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0

        for operation in operations:
            if operation in ['++X', 'X++']:
                x += 1

            else:
                x -= 1

        return x
        