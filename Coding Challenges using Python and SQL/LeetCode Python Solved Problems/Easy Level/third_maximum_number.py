# 414.) Third Maximum Number
# Categories: Array, Sorting

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)), reverse=True)

        try:
            return nums[2]
        
        except IndexError:
            return nums[0]