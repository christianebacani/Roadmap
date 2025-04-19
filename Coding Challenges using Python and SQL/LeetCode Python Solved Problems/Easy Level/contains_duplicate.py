# 217.) Contains Duplicate
# Categories: Array, Hash Table, Sorting

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        
        return True