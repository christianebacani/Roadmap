# 2643.) Row With Maximum Ones
# Categories: Array, Matrix

class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        ones_count = {}

        for i in range(len(mat)):
            ones_count[i] = mat[i].count(1)
    
        maximum_count = max(list(ones_count.values()), default=0)

        for index, count in ones_count.items():
            if maximum_count == count:
                return [index, count]
        