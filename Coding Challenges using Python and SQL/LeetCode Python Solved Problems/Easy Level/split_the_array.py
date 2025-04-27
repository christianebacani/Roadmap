# 3046.) Split the Array
# Categories: Array, Hash Table, Counting

from typing import List

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums.count(nums[i]) > 2:
                return False
        
        return True