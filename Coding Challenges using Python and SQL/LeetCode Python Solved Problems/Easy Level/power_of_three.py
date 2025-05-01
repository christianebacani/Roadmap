# 326.) Power of Three
# Categories: Math, Recursion

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(0, 101):
            if 3 ** i == n:
                return True
        
        return False