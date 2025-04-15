# 476.) Number Complement
# Categories: Bit Manipulation

class Solution:
    def findComplement(self, num: int) -> int:
        def convertToBinary(number: int) -> str:
            binary = ''

            while number > 0:
                remainder = number % 2
                binary = str(remainder) + binary
                number = number // 2
            
            return binary

        binary_equivalent = convertToBinary(num)
        complement = ''

        for i in range(len(binary_equivalent)):
            if binary_equivalent[i] == '1':
                complement += '0'
            
            else:
                complement += '1'
        
        return int(complement, 2)