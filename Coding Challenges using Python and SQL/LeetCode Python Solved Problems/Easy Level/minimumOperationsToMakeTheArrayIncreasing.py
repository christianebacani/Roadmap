# 1827.) Minimum Operations to Make the Array Increasing
# Categories: Array, Greedy

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        number_of_operations = 0

        if len(nums) == 1:
            return number_of_operations

        for i in range(1, len(nums)):
            previous_num = nums[i - 1]
            current_num = nums[i]
            
            if previous_num >= current_num:
                nums[i] = nums[i] + ((previous_num - current_num) + 1)
                number_of_operations += (previous_num - current_num) + 1

        return number_of_operations            
        

            
        