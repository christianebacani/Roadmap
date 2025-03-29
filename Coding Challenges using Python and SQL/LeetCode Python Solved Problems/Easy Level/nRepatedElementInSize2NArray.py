# 961.) N-Repeated Element in Size 2N Array
# Categories: Array, Hash Table

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            count = 0
            
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            
            if count > 1:
                return nums[i]
