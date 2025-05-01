# 231.) Power of Two
# Categories: Math, Bit Manipulation, Recursion

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(0, 100):
            if 2 ** i == n:
                return True
        
        return False