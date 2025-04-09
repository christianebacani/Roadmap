# 1837.) Sum of Digits in Base K
# Categories: Math

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def convertToGivenBase(number: int, base: int) -> int:
            remainders = []
            
            while number != 0:
                quotient = number // base
                remainder = number % base
    
                remainders.append(str(remainder))
                number = quotient
            
            return int(''.join(remainders[::-1]))
        
        converted_number = str(convertToGivenBase(n, k))
        sum = 0
        
        for i in range(len(converted_number)):
            sum += int(converted_number[i])
        
        return sum
            