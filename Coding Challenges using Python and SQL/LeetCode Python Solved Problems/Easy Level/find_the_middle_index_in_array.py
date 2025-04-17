# 1991.) Find the Middle Index in Array
# Categories: Array, Prefix Sum

class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        middle_indices = []

        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                middle_indices.append(i)
        
        return min(middle_indices, default=-1)