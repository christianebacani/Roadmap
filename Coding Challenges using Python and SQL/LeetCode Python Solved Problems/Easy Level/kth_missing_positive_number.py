# 1539.) Kth Missing Positive Number
# Categories: Array, Binary Search

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing_positive_numbers = []

        for i in range(1, 2000 + 1):
            if i not in arr:
                missing_positive_numbers.append(i)
        
        return missing_positive_numbers[k - 1]