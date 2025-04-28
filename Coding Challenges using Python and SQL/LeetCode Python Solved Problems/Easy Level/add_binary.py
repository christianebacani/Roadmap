# 67.) Add Binary
# Categories: Math, String, Bit Manipulation, Simulation

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def convertIntToBin(number: int) -> str:
            if number == 0:
                return '0'

            binary = ''
            
            while number > 0:
                remainder = number % 2
                binary = str(remainder) + binary
                number = number // 2
            
            return binary

        integer_equivalent_of_a = int(a, 2)
        integer_equivalent_of_b = int(b, 2)

        return convertIntToBin(integer_equivalent_of_a + integer_equivalent_of_b)