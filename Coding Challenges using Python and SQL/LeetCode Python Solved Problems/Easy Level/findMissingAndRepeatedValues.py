# 2965.) Find Missing and Repeated Values
# Categories: Array, Hash Table, Math, Matrix

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        number_of_arrays = len(grid)
        number_of_elements = len(grid[0])
        values = number_of_arrays * number_of_elements
    
        ans = []

        for i in range(1, values + 1):
            count = 0

            for lst in grid:
                for num in lst:
                    if i == num:
                        count += 1
        
            if count > 1:
                ans.append(i)

        for i in range(1, values + 1):
            missing_value = True

            for lst in grid:
                if i in lst:
                    missing_value = False

            if missing_value:
                ans.append(i)

        return ans
