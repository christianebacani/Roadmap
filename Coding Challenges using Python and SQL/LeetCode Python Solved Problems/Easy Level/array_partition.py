# 561.) Array Partition
# Categories: Array, Greedy, Sorting, Counting Sort

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        pairs = []
        
        for i in range(0, len(nums), 2):
            pairs.append(nums[i : i + 2])
        
        total_sum_of_min_pairs = 0

        for i in range(len(pairs)):
            total_sum_of_min_pairs += min(pairs[i])
        
        return total_sum_of_min_pairs