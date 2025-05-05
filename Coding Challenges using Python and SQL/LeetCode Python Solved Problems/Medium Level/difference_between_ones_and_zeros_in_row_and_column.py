# 2482.) Difference Between Ones and Zeros in Row and Column
# Categories: Array, Matrix, Simulation

from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        onesCol = []
        zerosRow = []
        zerosCol = []

        for i in range(len(grid)):
            onesRow.append(grid[i].count(1))
            zerosRow.append(grid[i].count(0))
        
        for i in range(len(grid[0])):
            column = []

            for j in range(len(grid)):
                column.append(grid[j][i])
            
            onesCol.append(column.count(1))
            zerosCol.append(column.count(0))
        
        diff = []
        
        for i in range(len(grid)):
            diff_row = []

            for j in range(len(grid[i])):
                diff_row.append(onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j])
            
            diff.append(diff_row)
        
        return diff