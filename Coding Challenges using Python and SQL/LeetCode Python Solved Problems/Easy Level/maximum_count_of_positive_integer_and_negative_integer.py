# 2529.) Maximum Count of Positive Integer and Negative Integer
# Categories: Array, Binary Search, Counting

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos = []
        neg = []

        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            
            elif nums[i] < 0:
                neg.append(nums[i])
            
        if len(pos) >= len(neg):
            return len(pos)
    
        return len(neg)
