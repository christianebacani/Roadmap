# 2194.) Cells in a Range on an Excel Sheet
# Categories: String

class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        columns = [
        'A', 'B', 'C',
        'D', 'E', 'F',
        'G', 'H', 'I',
        'J', 'K', 'L',
        'M', 'N', 'O',
        'P', 'Q', 'R',
        'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z'
        ]
        result = []

        for index, column in enumerate(columns):
            if s[0] == column:
                start_index = index
                
            if s[3] == column:
                last_index = index
                
        column_cells = columns[start_index:last_index + 1]
        start_row = int(s[1])
        last_row = int(s[4]) + 1
        
        for column_cell in column_cells:
            for row in range(start_row, last_row):
                cell = column_cell + str(row)
                result.append(cell)
        
        return result
