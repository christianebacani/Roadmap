# 1351.) Count Negative Numbers in a Sorted Matrix
# Categories: Array, Binary Search, Matrix

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
    
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count += 1
        
        return count
    