# 2089.) Find Target Indices After Sorting Array
# Categories: Array, Binary Search, Sorting

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        target_indices = []
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] == target:
                target_indices.append(i)
        
        return target_indices
        
