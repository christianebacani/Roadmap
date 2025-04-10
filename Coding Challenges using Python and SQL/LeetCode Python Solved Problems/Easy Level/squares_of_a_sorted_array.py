# 977.) Squares of a Sorted Array
# Categories: Array, Two Pointers, Sorting

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squared_nums = []

        for i in range(len(nums)):
            squared_nums.append(nums[i] ** 2)

        squared_nums = sorted(squared_nums)
        
        return squared_nums