# 3300.) Minimum Element After Replacement With Digit Sum
# Category: Array, Math

class Solution:
    def minElement(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            num = str(nums[i])
            sum_of_num = 0

            for j in range(len(num)):
                sum_of_num += int(num[j])
        
            nums[i] = sum_of_num
    
        return min(nums)
