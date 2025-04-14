# 1331.) Rank Transform of an Array
# Categories: Array, Hash Table, Sorting

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_distinct_elements = sorted(set(arr))
        rankings = {}

        for i in range(len(sorted_distinct_elements)):
            rankings[sorted_distinct_elements[i]] = i + 1

        answer = []

        for i in range(len(arr)):
            answer.append(rankings[arr[i]])
        
        return answer