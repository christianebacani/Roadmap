# 1200.) Minimum Absolute Difference
# Categories: Array, Sorting

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr = sorted(arr)
        absolute_differences = {}

        for i in range(len(arr) - 1):
            absolute_differences[tuple([arr[i], arr[i + 1]])] = abs(arr[i] - arr[i + 1])
        
        minimum_absolute_difference = min(list(absolute_differences.values()))
        result = []
        
        for pair, absolute_difference in absolute_differences.items():
            if minimum_absolute_difference == absolute_difference:
                result.append(list(pair))

        return result