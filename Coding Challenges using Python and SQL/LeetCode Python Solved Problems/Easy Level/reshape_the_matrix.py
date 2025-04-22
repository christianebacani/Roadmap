# 566.) Reshape the Matrix
# Categories: Array, Matrix, Simulation

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        number_of_rows = len(mat)
        number_of_columns = len(mat[0])

        if number_of_rows * number_of_columns != r * c:
            return mat
        
        elements = []

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                elements.append(mat[i][j])
        
        reshaped_mat = []

        for i in range(0, len(elements), c):
            sub_array = elements[i : i + c]
            reshaped_mat.append(sub_array)
        
        return reshaped_mat
