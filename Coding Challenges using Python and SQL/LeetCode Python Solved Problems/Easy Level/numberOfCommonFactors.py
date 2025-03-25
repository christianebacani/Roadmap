# 2427.) Number of Common Factors
# Categories: Math, Enumeration, Number Theory

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        common_factors = []
        
        for i in range(1, 1001):
            if (a % i == 0) and (b % i == 0):
                common_factors.append(i)
        
        return len(common_factors)
    