# 724.) Find Pivot Index
# Categories: Array, Prefx Sum

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            left_nums_of_current_index = nums[:i]
            right_nums_of_current_index = nums[i + 1:]

            if sum(left_nums_of_current_index) == sum(right_nums_of_current_index):
                return i
        
        return -1