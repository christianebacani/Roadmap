# 1389.) Create Target Array in the Given Order
# Categories: Array, Simulation

class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target_array = []

        for i in range(len(nums)):
            target_array.insert(index[i], nums[i])
    
        return target_array
