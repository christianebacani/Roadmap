# 3364.) Minimum Positive Sum Subarray
# Categories: Array, Sliding Window, Prefix Sum

from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        subarray_sums = []

        for i in range(l, r + 1):
            for j in range(len(nums)):
                subarray = nums[j : j + i]

                if len(subarray) != i:
                    continue

                if sum(subarray) <= 0:
                    continue

                subarray_sums.append(sum(subarray))
        
        return min(subarray_sums, default=-1)