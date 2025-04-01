# 136.) Single Number
# Categories: Array, Bit Manipulation

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        distinct_nums = list(set(nums))

        for i in range(len(distinct_nums)):
            frequency = nums.count(distinct_nums[i])
            
            if frequency == 1:
                return distinct_nums[i]
        
