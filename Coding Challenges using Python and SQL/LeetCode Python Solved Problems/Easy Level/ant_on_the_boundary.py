# 3028.) Ant on the Boundary
# Categories: Array, Simulation, Prefix Sum

class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        count = 0
        current_steps = 0
        
        for i in range(len(nums)):
            if nums[i] > 0:
                current_steps += nums[i]

            else:
                current_steps -= (nums[i] * -1)

            if current_steps == 0:
                count += 1
        
        return count
