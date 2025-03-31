# 461.) Hamming Distance
# Categories: Bit Manipulation

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def convertToBinary(number: int) -> str:
            binary = ''
            
            while number > 0:
                remainder = number % 2
                binary = str(remainder) + binary
                number = number // 2
            
            return binary
        
        binary_x = convertToBinary(x)
        binary_y = convertToBinary(y)
        count = 0
        
        if len(binary_x) > len(binary_y):
            difference = len(binary_x) - len(binary_y)
            binary_y = (difference * '0') + binary_y
        
        elif len(binary_y) > len(binary_x):
            difference = len(binary_y) - len(binary_x)
            binary_x = (difference * '0') + binary_x

        for i in range(len(binary_x)):
            for j in range(len(binary_y)):
                if (i == j) and (binary_x[i] != binary_y[i]):
                    count += 1
    
        return count
