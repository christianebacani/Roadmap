# 3095.) Shortest Subarray With Or at Least K I
# Categories: Array, Bit Manipulation, Sliding Window

from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        length_of_subarray = []

        for i in range(1, len(nums) + 1):
            for j in range(len(nums)):
                subarray = nums[j : j + i]

                if len(subarray) != i:
                    continue

                total_bitwise_or = subarray[0]

                for element in subarray:
                    total_bitwise_or |= element
                
                if total_bitwise_or >= k:
                    length_of_subarray.append(len(subarray))

        return min(length_of_subarray, default=-1)