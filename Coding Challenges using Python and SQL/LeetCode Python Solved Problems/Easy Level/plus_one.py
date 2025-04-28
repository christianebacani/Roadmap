# 66.) Plus One
# Categories: Array, Math

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        large_digits = ''
        
        for i in range(len(digits)):
            large_digits += str(digits[i])
        
        large_digits = list(str(int(large_digits) + 1))
        large_digits = [int(num) for num in large_digits]

        return large_digits