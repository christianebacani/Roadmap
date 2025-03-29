# 1295.) Find Numbers with Even Number of Digits
# Categories: Array, Math

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count += 1
        
        return count