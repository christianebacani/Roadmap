# 2006.) Count Number of Pairs With Absolute Difference K
# Categories: Array, Hash Table, Counting

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        pairs = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i < j) and (abs(nums[i] - nums[j]) == k):
                    pairs.append(tuple([nums[i], nums[j]]))
    
        return len(pairs)
