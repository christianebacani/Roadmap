# 2859.) Sum of Values at Indices With K Set Bits
# Categories: Array, Bit Manipulation

class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        def convertToBinary(n: int) -> str:
            binary = ''
            while n > 0:
                remainder = n % 2
                binary = f'{remainder}{binary}'
                n = n // 2
        
            return binary
    
        sum = 0

        for i in range(len(nums)):
            binary_index = convertToBinary(i)
            bits_count = binary_index.count('1')
            
            if bits_count == k:
                sum += nums[i]

        return sum
