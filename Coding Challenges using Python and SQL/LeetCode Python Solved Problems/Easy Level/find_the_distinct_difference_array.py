# 2670.) Find the Distinct Difference Array
# Categories: Array, Hash Table

class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        result = []
        
        for i in range(len(nums)):
            prefix = list(set(nums[:i + 1]))
            suffix = list(set(nums[i + 1:]))
            
            difference = len(prefix) - len(suffix)
            result.append(difference)
    
        return result
    