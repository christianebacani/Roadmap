# 896.) Monotonic Array
# Categories: Array

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if sorted(nums) == nums or sorted(nums, reverse=True) == nums:
            return True
        
        return False