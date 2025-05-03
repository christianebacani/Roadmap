# 3487.) Maximum Unique Subarray Sum After Deletion
# Categories: Array, Hash Table, Greedy

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_after_deletion = []

        for i in range(len(nums)):
            if nums[i] < 0:
                continue

            if nums[i] in nums_after_deletion:
                continue

            nums_after_deletion.append(nums[i])
        
        if nums_after_deletion == []:
            return max(nums)
        
        return sum(nums_after_deletion)