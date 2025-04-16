# 2639.) Find the Width of Columns of a Grid
# Categories: Array, Matrix

class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        total_columns = len(grid[0])
        columns = []

        for i in range(total_columns):
            column = []

            for j in range(len(grid)):
                column.append(grid[j][i])

            columns.append(column)
        
        answer = []

        for i in range(len(columns)):
            length_of_column = []

            for j in range(len(columns[i])):
                length_of_column.append(len(str(columns[i][j])))
            
            answer.append(max(length_of_column))
        
        return answer