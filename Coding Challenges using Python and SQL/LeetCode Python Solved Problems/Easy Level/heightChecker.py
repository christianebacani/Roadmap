# 1051.) Height Checker
# Categories: Array, Sorting, Counting Sort

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        count = 0

        for i in range(len(expected)):
            for j in range(len(heights)):
                if (i == j) and (expected[i] != heights[j]):
                    count += 1
        
        return count