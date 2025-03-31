# 905.) Sort Array By Parity
# Categories: Array, Two Pointers, Sorting

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        odd = [num for num in nums if num % 2 != 0]
        even = [num for num in nums if num % 2 == 0]
    
        return even + odd
    
    
        