# 1480.) Running Sum of 1d Array
# Categories: Array, Prefix Sum

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum_of_nums = []

        for i in range(len(nums)):
            sum_of_current_nums = sum(nums[:i + 1])
            sum_of_nums.append(sum_of_current_nums)

        return sum_of_nums

