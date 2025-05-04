# 2610.) Convert an Array Into a 2D Array With Conditions
# Categories: Array, Hash Table

from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums_2d = []

        while len(nums) != 0:
            current_row = []
            new_nums = []

            for i in range(len(nums)):
                if nums[i] not in current_row:
                    current_row.append(nums[i])
                
                else:
                    new_nums.append(nums[i])
            
            nums_2d.append(current_row)
            nums = new_nums
        
        return nums_2d