# 867.) Transpose Matrix
# Categories: Array, Matrix, Simulation

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        total_number_of_columns = len(matrix[0])
        transposed_matrix = []

        for i in range(total_number_of_columns):
            row = []
    
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            
            transposed_matrix.append(row)

        return transposed_matrix