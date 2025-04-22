# 757.) Largest Number At Least Twice of Others
# Categories: Array, Sorting

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest_element = max(nums)
        
        for i in range(len(nums)):
            if nums[i] == largest_element:
                continue

            if nums[i] * 2 > largest_element:
                return -1
        
        return nums.index(largest_element)