# Question: Matrix Addition
# Categories: 6 Kyu

def matrix_addition(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    result = []

    for i in range(len(a)):
        row = []

        for j in range(len(a[i])):
            row.append(a[i][j] + b[i][j])
        
        result.append(row)
    
    return result