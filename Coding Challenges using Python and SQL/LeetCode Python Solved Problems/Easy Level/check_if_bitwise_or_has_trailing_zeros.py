# 2980.) Check if Bitwise OR Has Trailing Zeros
# Categories: Array, Bit Manipulation

class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                if nums[i] % 2 != 0 or nums[j] % 2 != 0:
                    continue

                if bin(nums[i] ^ nums[j])[2:].endswith('0'):
                    return True

        return False