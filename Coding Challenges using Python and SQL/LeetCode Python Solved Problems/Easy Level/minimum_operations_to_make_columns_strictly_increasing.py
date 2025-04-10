# 3402.) Minimum Operations to Make Columns Strictly Increasing
# Categories: Array, Greedy, Matrix

class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        total_number_of_columns = len(grid[0])
        columns = []

        for column in range(total_number_of_columns):
            values = []
            
            for row in grid:
                values.append(row[column])
            
            columns.append(values)
    
        number_of_operations = 0
        
        for i in range(len(columns)):
            for j in range(1, len(columns[i])):
                if columns[i][j - 1] >= columns[i][j]:
                    number_of_operations += ((columns[i][j - 1] - columns[i][j]) + 1)
                    columns[i][j] += ((columns[i][j - 1] - columns[i][j]) + 1)
    
        return number_of_operations
