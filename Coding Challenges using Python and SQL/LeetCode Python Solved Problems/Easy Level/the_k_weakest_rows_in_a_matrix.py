# 1337.) The K Weakest Rows in a Matrix
# Categories: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        number_of_soldiers = {}

        for i in range(len(mat)):
            number_of_soldiers[i] = mat[i].count(1)
        
        distinct_sorted_number_of_soldiers = sorted(set(number_of_soldiers.values()))
        result = []
        
        for i in range(len(distinct_sorted_number_of_soldiers)):
            for index, number_of_soldier in number_of_soldiers.items():
                if distinct_sorted_number_of_soldiers[i] == number_of_soldier:
                    result.append(index)
        
        return result[:k]
