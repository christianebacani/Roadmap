# Question: Put a Letter in a Column
# Categories: 7 Kyu

def build_row_text(index: int, character: str) -> str:
    columns = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    columns[index] = character
    columns = '|'.join(columns)
    columns = '|' + columns + '|'

    return columns