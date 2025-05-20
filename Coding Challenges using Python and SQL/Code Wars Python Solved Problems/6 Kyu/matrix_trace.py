# Question: Matrix Trace
# Categories: 6 Kyu

def is_matrix_valid(mat: list[list[int]]) -> bool:
    if mat == []:
        return False

    rows = len(mat)
    columns = len(mat[0])

    if rows == columns:
        return True
    
    return False

def trace(matrix: list[list[int]]) -> int:
    if not is_matrix_valid(matrix):
        return None
    
    trace = []

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                continue

            trace.append(matrix[j][j])
    
    return sum(trace)