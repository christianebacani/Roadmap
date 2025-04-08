# 191.) Number of 1 Bits
# Categories: Divide and Conquer and Bit Manipulation

class Solution:
    def hammingWeight(self, n: int) -> int:
        def getBinaryValue(num: int) -> str:
            binary = ''
            
            while num > 0:
                remainder = num % 2
                binary = str(remainder) + binary
                num = num // 2
            
            return binary
        
        number_of_set_bits = getBinaryValue(n).count('1')
        
        return number_of_set_bits