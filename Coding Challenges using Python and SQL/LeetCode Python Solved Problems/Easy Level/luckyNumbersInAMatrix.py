# 1380.) Lucky Numbers in a Matrix
# Categories: Array, Matrix

class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        minimum_elements_from_row = []
        maximum_elements_from_column = []

        for row in matrix:
            minimum_elements_from_row.append(min(row))

        for column_position in range(len(matrix[0])):
            column = []

            for row in matrix:
                column.append(row[column_position])
    
            maximum_elements_from_column.append(max(column))

        lucky_numbers = []

        for row_index, row in enumerate(matrix):
            for column_index, element in enumerate(row):
                if (element == minimum_elements_from_row[row_index]) and (element == maximum_elements_from_column[column_index]):
                    lucky_numbers.append(element)
        
        return lucky_numbers
