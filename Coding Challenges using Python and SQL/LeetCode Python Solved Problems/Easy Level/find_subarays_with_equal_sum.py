# 2395.) Find Subarrays With Equal Sum

class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        subarray_sums = []
        
        for i in range(1, len(nums)):
            subarray_sums.append(nums[i - 1] + nums[i])
        
        for i in range(len(subarray_sums)):
            if subarray_sums.count(subarray_sums[i]) >= 2:
                return True
        
        return False