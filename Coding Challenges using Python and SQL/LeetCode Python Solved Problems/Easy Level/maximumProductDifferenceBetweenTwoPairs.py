# 1913.) Maximum Product Difference Between Two Pairs
# Categories: Array, Sorting

class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums = sorted(nums, reverse=True)
        maximum_number_pair = nums[:2]
        minimum_number_pair = nums[-2:]

        return (maximum_number_pair[0] * maximum_number_pair[1]) - (minimum_number_pair[0] * minimum_number_pair[1])
        
