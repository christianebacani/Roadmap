# 2413.) Smallest Even Multiple
# Categories: Math, Number Theory

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiples = []

        for i in range(1, 1000):
            if i % 2 == 0 and i % n == 0:
                multiples.append(i)
        
        return min(multiples)