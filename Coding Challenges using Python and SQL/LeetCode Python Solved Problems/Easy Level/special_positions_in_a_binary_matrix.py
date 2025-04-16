# 1582.) Special Positions in a Binary Matrix
# Categories: Array, Matrix

class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        count = 0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] != 1:
                    continue

                if mat[i].count(1) != 1:
                    break
                
                column = []

                for k in range(len(mat)):
                    column.append(mat[k][j])
                
                if column.count(1) == 1:
                    count += 1
        
        return count