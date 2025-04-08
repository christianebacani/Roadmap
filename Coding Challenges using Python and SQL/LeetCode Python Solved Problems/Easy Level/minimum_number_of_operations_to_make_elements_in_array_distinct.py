# 3396.) Minimum Number of Operations to Make Elements in Array Distinct
# Categories: Array, Hash Table

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        count = 0

        while len(set(nums)) != len(nums):
            if len(nums) >= 3:
                nums = nums[3:]
            
            else:
                nums = []

            count += 1
    
        return count
    