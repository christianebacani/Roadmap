# 1252.) Cells with Odd Values in a Matrix
# Categories: Array, Math, Simulation

from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = []

        for _ in range(m):
            row = []
            
            for _ in range(n):
                row.append(0)
            
            matrix.append(row)
        
        for i in range(len(indices)):
            row_to_increment = indices[i][0]
            column_to_increment = indices[i][1]

            for j in range(len(matrix)):
                if row_to_increment != j:
                    continue

                for k in range(len(matrix[j])):
                    matrix[j][k] += 1

            for j in range(len(matrix)):
                for k in range(len(matrix[j])):
                    if column_to_increment != k:
                        continue

                    matrix[j][k] += 1
        
        number_of_odd_values = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] % 2 != 0:
                    number_of_odd_values += 1
        
        return number_of_odd_values