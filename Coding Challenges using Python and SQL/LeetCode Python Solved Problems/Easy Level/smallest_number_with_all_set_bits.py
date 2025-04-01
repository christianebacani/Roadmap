# 3370.) Smallest Number With All Set Bits
# Categories: Math, Bit Manipulation

class Solution:
    def smallestNumber(self, n: int) -> int:
        def convertToBinary(number: int) -> str:
            binary = ''
            
            while number > 0:
                remainder = number % 2
                binary = str(remainder) + binary
                number = number // 2
            
            return binary
        
        while True:
            binary_equivalent = convertToBinary(n)

            if '0' not in binary_equivalent:
                answer = n
                break
            
            n += 1

        return answer

