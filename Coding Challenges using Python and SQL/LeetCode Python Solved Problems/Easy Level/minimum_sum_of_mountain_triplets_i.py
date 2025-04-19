# 2908.) Minimum Sum of Mountain Triplets I
# Categories: Array

class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        sum_of_mountain_triplets = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (i < j < k) and (nums[i] < nums[j] and nums[k] < nums[j]):
                        sum_of_mountain_triplets.append(nums[i] + nums[j] + nums[k])
        
        return min(sum_of_mountain_triplets, default=-1)