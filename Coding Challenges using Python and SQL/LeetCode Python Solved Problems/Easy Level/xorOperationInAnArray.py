# 1486.) XOR Operation in an Array
# Categories: Math, Bit Manipulation

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
    
        for i in range(n):
            nums.append(start + 2 * i)
    
        total_xor = nums[0]

        for i in range(1, len(nums)):
            total_xor ^= nums[i]

        return total_xor
