# 3038.) Maximum Number of Operations With the Same Score I
# Categories: Array, Simulation

from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        number_of_operations = 0
        sums = []

        while len(nums) >= 2:
            if sums == []:
                sums.append(nums[0] + nums[1])
                nums = nums[2:]
                number_of_operations += 1
                continue


            if nums[0] + nums[1] not in sums:
                break
            
            else:
                sums.append(nums[0] + nums[1])
                nums = nums[2:]
                number_of_operations += 1


        return number_of_operations