# 1909.) Remove One Element to Make the Array Strictly Increasing
# Categories: Remove One Element to Make the Array Strictly Increasing

from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def isArrayStrictlyIncreasing(arr: List[int]) -> bool:
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            
            return True

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    continue

                previous_numbers = nums[:j]
                next_numbers = nums[j + 1:]
                
                if isArrayStrictlyIncreasing(previous_numbers + next_numbers):
                    return True

        return False