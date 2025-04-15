# 3252.) Sum of Good Numbers
# Categories: Array

class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        first_index = 0
        last_index = len(nums) - 1
        sum = 0
    
        for i in range(len(nums)):
            if (i - k < first_index):
                previous_element = 0

            else:
                previous_element = nums[i - k]
            
            
            if (i + k > last_index):
                next_element = 0
    
            else:
                next_element = nums[i + k]

            
            if nums[i] > previous_element and nums[i] > next_element:
                sum += nums[i]

        return sum