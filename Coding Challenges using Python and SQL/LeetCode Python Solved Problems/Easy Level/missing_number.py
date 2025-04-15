# 268.) Missing Number
# Categories: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i