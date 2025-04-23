# 693.) Binary Number with Alternating Bits
# Categories: Bit Manipulation

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def convertToBinary(number: int) -> str:
            binary_value = ''

            while number > 0:
                remainder = number % 2
                binary_value = str(remainder) + binary_value
                number = number // 2
            
            return binary_value
        
        binary = convertToBinary(n)

        for i in range(1, len(binary)):
            if binary[i - 1] == binary[i]:
                return False
        
        return True