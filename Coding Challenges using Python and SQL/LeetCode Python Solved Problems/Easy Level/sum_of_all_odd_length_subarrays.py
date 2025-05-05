# 1588.) Sum of All Odd Length Subarrays
# Categories: Array, Math, Prefix Sum

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0

        for i in range(1, len(arr) + 1):
            if i % 2 == 0:
                continue

            for j in range(len(arr)):
                subarray = arr[j : j + i]

                if len(subarray) != i:
                    continue

                total_sum += sum(subarray)

        return total_sum