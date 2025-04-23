# 1952.) Three Divisors
# Categories: Math, Enumeration, Number Theory

class Solution:
    def isThree(self, n: int) -> bool:
        positive_divisors = []

        for i in range(1, n + 1):
            if n % i == 0:
                positive_divisors.append(i)
        
        if len(positive_divisors) == 3:
            return True
        
        return False