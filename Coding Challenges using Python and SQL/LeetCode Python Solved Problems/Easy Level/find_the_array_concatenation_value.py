# 2562.) Find the Array Concatenation Value
# Categories: Array, Two Pointers, Simulation

class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        value = 0

        while len(nums) != 0:
            if len(nums) == 1:
                value += nums[0]
                nums.pop(0)
            
            else:
                value += (int(str(nums[0]) + str(nums[-1])))
                nums.pop(0)
                nums.pop(-1)

        return value