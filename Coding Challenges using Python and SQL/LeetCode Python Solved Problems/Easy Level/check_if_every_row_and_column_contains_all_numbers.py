# 2133.) Check if Every Row and Column Contains All Numbers
# Categories: Array, Hash Table, Matrix

from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        columns = []
        rows = []

        total_columns = len(matrix[0])
        
        for i in range(total_columns):
            column = []

            for j in range(len(matrix)):
                column.append(matrix[j][i])
            
            columns.append(column)

        for i in range(len(matrix)):
            row = []

            for j in range(len(matrix[i])):
                row.append(matrix[i][j])
            
            rows.append(row)
        
        n = len(matrix) + 1

        for i in range(1, n):
            for column in columns:
                if i not in column:
                    return False

            for row in rows:
                if i not in row:
                    return False
        
        return True