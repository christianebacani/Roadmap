# 2418.) Sort the People
# Categories: Array, Hash Table, String, Sorting

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        height_with_name = {}

        for i in range(len(names)):
            for j in range(len(heights)):
                if i == j:
                    height_with_name[heights[j]] = names[i]

        heights = sorted(heights, reverse=True)
        result = []

        for height in heights:
            result.append(height_with_name[height])
    
        return result
