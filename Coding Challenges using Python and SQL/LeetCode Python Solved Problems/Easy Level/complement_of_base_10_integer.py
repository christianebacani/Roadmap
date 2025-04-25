# 1009.) Complement of Base 10 Integer
# Categories: Bit Manipulation

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        def convertNumToBin(number: int) -> str:
            binary = ''

            while number > 0:
                remainder = number % 2
                binary = str(remainder) + binary
                number = number // 2
            
            return binary

        if n == 0:
            return 1

        binary_value = convertNumToBin(n)
        complement_binary_value = ''

        for i in range(len(binary_value)):
            if binary_value[i] == '0':
                complement_binary_value += '1'
            
            else:
                complement_binary_value += '0'
        
        return int(complement_binary_value, 2)