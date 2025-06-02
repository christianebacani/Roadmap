# Question: Matrix Transpose
# Categories: 6 Kyu

def transpose(matrix: list[list[int]]) -> list[list[int]]:
    if matrix == [[]]:
        return [[]]
    
    total_columns = len(matrix[0])
    transposed_matrix = []

    for i in range(total_columns):
        row = []

        for j in range(len(matrix)):
            row.append(matrix[j][i])
        
        transposed_matrix.append(row)
    
    return transposed_matrix