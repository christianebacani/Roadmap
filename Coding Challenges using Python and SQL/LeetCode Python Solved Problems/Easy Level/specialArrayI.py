# 3141.) Special Array I
# Categories: Array

class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        
        for i in range(1, len(nums)):
            pair = nums[i - 1 : i + 1]
            
            if (pair[0] % 2 == 0) and (pair[1] % 2 == 0):
                return False
            
            if (pair[0] % 2 != 0) and (pair[1] % 2 != 0):
                return False
        
        return True

            
    
            