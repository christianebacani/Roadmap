# 2733.) Neither Mininum nor Maximum
# Categories: Array, Sorting

class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        
        for i in range(len(nums)):
            if min_num != nums[i] and max_num != nums[i]:
                return nums[i]
    
        return -1
    
        
        