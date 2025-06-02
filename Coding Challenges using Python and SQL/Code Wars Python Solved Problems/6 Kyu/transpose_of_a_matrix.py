# Question: Transpose of a Matrix
# Categories: 6 Kyu

def transpose(arr: list[list[int]]) -> list[list[int]]:
    if arr == [[]]:
        return [[]]

    total_columns = len(arr[0])
    transposed_matrix = []

    for i in range(total_columns):
        column = []

        for j in range(len(arr)):
            column.append(arr[j][i])

        transposed_matrix.append(column)

    return transposed_matrix