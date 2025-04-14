# 762.) Prime Numbers of Set Bits in Binary Representation
# Categories: Math, Bit Manipulation

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0

        for i in range(left, right + 1):
            set_bits = bin(i)[2:].count('1')
            prime = True

            if set_bits == 1:
                continue
            
            elif set_bits == 2:
                count += 1
                continue

            for j in range(2, set_bits):
                if set_bits % j == 0:
                    prime = False
                    break
            
            if prime:
                count += 1
        
        return count