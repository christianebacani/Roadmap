# 3033.) Modify the Matrix
# Categories: Array, Matrix

class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        answer = []

        for i in range(len(matrix)):
            row = []

            for j in range(len(matrix[i])):
                if matrix[i][j] != -1:
                    row.append(matrix[i][j])
                    continue

                column = []

                for k in range(len(matrix)):
                    if i != k:
                        column.append(matrix[k][j])
                
                row.append(max(column))
        
            answer.append(row)
        
        return answer