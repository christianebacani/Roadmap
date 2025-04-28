# 2855.) Minimum Right Shifts to Sort the Array
# Categories: Array

from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        if sorted_nums == nums:
            return 0
        
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

            if nums == sorted_nums:
                return number_of_shifts
        
        return -1