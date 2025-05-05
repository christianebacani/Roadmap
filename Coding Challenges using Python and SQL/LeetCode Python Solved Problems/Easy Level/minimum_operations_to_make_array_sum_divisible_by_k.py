# 3512.) Minimum Operations to Make Array Sum Divisible by K
# Categories: Array, Math

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        number_of_operations = 0

        while total_sum % k != 0:
            total_sum -= 1
            number_of_operations += 1

        return number_of_operations