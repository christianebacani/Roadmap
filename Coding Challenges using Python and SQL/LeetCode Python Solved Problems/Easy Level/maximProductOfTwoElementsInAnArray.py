# 1464.) Maximum Product of Two Elements in an Array
# Categories: Array, Sorting, Heap(Priority Queue)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        sorted_desc_nums = sorted(nums, reverse=True)
        maximum_number = sorted_desc_nums[0]
        second_maximum_number = sorted_desc_nums[1]

        return (maximum_number - 1) * (second_maximum_number - 1)
