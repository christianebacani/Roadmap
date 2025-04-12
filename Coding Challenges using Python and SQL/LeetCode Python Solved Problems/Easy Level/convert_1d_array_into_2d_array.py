# 2022.) Convert 1D Array Into 2D Array
# Categories: Array, Matrix, Simulation

class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
    
        answer = []

        for i in range(0, len(original), n):
            row = original[i:i + n]
            answer.append(row)

        return answer