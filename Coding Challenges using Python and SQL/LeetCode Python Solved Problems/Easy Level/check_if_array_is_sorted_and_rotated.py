# 1752.) Check if Array Is Sorted and Rotated
# Categories: Array

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        number_of_shifts = 0

        while number_of_shifts < len(nums):
            shifted_nums = []

            for i in range(len(nums)):
                if i == len(nums) - 1:
                    shifted_nums.insert(0, nums[i])
                
                else:
                    shifted_nums.insert(i + 1, nums[i])
            
            nums = shifted_nums
            number_of_shifts += 1

            if nums == sorted(nums):
                return True
        
        return False