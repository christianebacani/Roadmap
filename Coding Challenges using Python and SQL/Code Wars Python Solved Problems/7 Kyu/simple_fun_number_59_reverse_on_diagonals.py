# Question: Simple Fun #59: Reverse On Diagonals
# Categories: 7 Kyu

def reverse_on_diagonals(matrix: list[list[int]]) -> list[list[int]]:
    first_longest_diagonal, second_longest_diagonal = [], []
    total_rows = len(matrix)

    for i in range(total_rows):
        first_longest_diagonal.append(matrix[i][i])
        second_longest_diagonal.append(matrix[i][::-1][i])
    
    first_longest_diagonal, second_longest_diagonal = first_longest_diagonal[::-1], second_longest_diagonal[::-1]

    for i in range(total_rows):
        matrix[i][i] = first_longest_diagonal[0]
        first_longest_diagonal = first_longest_diagonal[1:]
    
    for i in range(total_rows):
        matrix[i] = matrix[i][::-1]
    
    for i in range(total_rows):
        matrix[i][i] = second_longest_diagonal[0]
        second_longest_diagonal = second_longest_diagonal[1:]
    
    for i in range(total_rows):
        matrix[i] = matrix[i][::-1]
    
    return matrix