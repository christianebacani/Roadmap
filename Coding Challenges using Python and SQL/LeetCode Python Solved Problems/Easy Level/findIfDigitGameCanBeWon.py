# 3232.) Find if Digit Game Can Be Won
# Categories: Array, Math

class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        sum_of_all_single_digits = 0
        sum_of_all_double_digits = 0
        
        for i in range(len(nums)):
            if nums[i] < 10:
                sum_of_all_single_digits += nums[i]

            else:
                sum_of_all_double_digits += nums[i]
        
        if (sum_of_all_single_digits > sum_of_all_double_digits) or (sum_of_all_double_digits > sum_of_all_single_digits):
            return True
        
        return False
    