# 1822.) Sign of the Product of an Array
# Categories: Array, Math

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        def signFunc(x: int) -> int:
            if x > 0:
                return 1
            
            elif x < 0:
                return -1
            
            return 0
        
        product = nums[0]

        for i in range(1, len(nums)):
            product *= nums[i]
        
        return signFunc(product)