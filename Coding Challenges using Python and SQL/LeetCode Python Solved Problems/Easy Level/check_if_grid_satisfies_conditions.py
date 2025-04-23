# 3142.) Check if Grid Satisfies Conditions
# Categories: Array, Matrix

class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                try:
                    if grid[i][j] != grid[i + 1][j]:
                        return False
                
                except IndexError:
                    pass

                try:
                    if grid[i][j] == grid[i][j + 1]:
                        return False
        
                except IndexError:
                    pass

        return True