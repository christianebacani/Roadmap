# 2057.) Smallest Index With Equal Value
# Categories: Array

class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
    
        return -1
    