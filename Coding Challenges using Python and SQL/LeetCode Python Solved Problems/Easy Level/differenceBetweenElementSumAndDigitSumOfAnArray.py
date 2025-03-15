# 2535.) Difference Between Element Sum and Digit Sum of an Array
# Categories: Array, Math

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            num = str(num)
            num_sum = 0
    
            for digit in num:
                num_sum += int(digit)
        
            digit_sum += num_sum

        return abs(element_sum - digit_sum)
