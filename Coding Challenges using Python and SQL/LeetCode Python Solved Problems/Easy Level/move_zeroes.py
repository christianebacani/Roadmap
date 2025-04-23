# 283.) Move Zeroes
# Categories: Array, Two Pointers

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number_of_zero_elements = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                number_of_zero_elements += 1
    
        for i in range(number_of_zero_elements):
            nums.remove(0)

        for i in range(number_of_zero_elements):
            nums.append(0)