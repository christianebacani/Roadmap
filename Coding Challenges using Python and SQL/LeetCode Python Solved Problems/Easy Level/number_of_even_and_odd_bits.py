# 2595.) Number of Even and Odd Bits
# Categories: Bit Manipulation

class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        def convertToBinary(number: int) -> str:
            binary = ''

            while number > 0:
                remainder = number % 2
                binary = str(remainder) + binary
                number = number // 2
            
            return binary

        binary_equivalent = convertToBinary(n)[::-1]
        even = 0
        odd = 0

        for i in range(len(binary_equivalent)):
            if (binary_equivalent[i] == '1') and (i % 2 == 0):
                even += 1

            elif (binary_equivalent[i] == '1') and (i % 2 != 0):
                odd += 1

        return [even, odd]       