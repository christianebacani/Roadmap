# 3345.) Smallest Divisible Digit Product I
# Categories: Math, Enumeration

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 101):
            i = list(str(i))
            product_of_each_digit = 1
            
            for j in range(len(i)):
                product_of_each_digit *= int(i[j])
            
            if product_of_each_digit % t == 0:
                return int(''.join(i))