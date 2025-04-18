# 1800.) Maximum Ascending Subarray Sum
# Categories: Array

class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        subarray_sums = []

        for i in range(len(nums)):
            subarray = [nums[i]]
    
            for j in range(len(nums)):
                if i < j and subarray[-1] < nums[j]:
                    subarray.append(nums[j])
    
                elif i < j and subarray[-1] >= nums[j]:
                    break
            
            subarray_sums.append(sum(subarray))
        
        return max(subarray_sums)