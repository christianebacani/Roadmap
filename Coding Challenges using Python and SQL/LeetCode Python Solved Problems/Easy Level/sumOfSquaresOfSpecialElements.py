# 2778.) Sum of Squares of Special Elements
# Categories: Array, Enumeration

class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        sum_of_squares = 0

        for index, num in enumerate(nums):
            index += 1
        
            if len(nums) % index == 0:
                sum_of_squares += num ** 2
    
        return sum_of_squares
