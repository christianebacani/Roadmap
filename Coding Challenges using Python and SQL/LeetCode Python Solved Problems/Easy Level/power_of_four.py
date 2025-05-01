# 342.) Power of Four
# Categories: Math, Bit Manipulation, Recursion

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(0, 101):
            if 4 ** i == n:
                return True
        
        return False