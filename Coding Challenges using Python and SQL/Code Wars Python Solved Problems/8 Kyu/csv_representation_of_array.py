# Question: CSV representation of array
# Categories: 8 Kyu

def to_csv_text(array: list[list[int]]) -> str:
    result = ''

    for i in range(len(array)):
        row = []

        for j in range(len(array[i])):
            row.append(str(array[i][j]))
        
        row = ','.join(row)

        if i == len(array) - 1:
            result += row
        
        else:
            result += row
            result += '\n'
    
    return result