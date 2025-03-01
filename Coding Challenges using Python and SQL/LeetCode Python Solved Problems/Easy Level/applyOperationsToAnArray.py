# 2460.) Apply Operations to an Array
# Categories : Array, Two Pointers, Simulation

class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1] = nums[i - 1] * 2
                nums[i] = 0

        new_nums = []
    
        for num in nums:
            if num != 0:
                new_nums.append(num)

        for num in nums:
            if num == 0:
                new_nums.append(num)
    
        return new_nums