# 2441.) Largest Positive Integer That Exists With Its Negative
# Categories: Array, Hash Table, Two Pointers, Sorting

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums = sorted(nums, reverse=True)
    
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (nums[i] != nums[j]) and (int(str(nums[i]).replace('-', '')) - int(str(nums[j]).replace('-', '')) == 0):
                    return nums[i]
        
        return -1
