# 2815.) Max Pair Sum in an Array
# Categories: Array, Hash Table

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        largest_digits = []

        for i in range(len(nums)):
            numbers = str(nums[i])
            largest_digit = 0
            
            for j in range(len(numbers)):
                if int(numbers[j]) > largest_digit:
                    largest_digit = int(numbers[j])
            
            largest_digits.append(largest_digit)
        
        sum_per_pairs_with_same_largest_digits = []

        for i in range(len(largest_digits)):
            for j in range(len(largest_digits)):
                if i == j:
                    continue

                if largest_digits[i] == largest_digits[j]:
                    sum_per_pairs_with_same_largest_digits.append(nums[i] + nums[j])
        
        return max(sum_per_pairs_with_same_largest_digits, default=-1)