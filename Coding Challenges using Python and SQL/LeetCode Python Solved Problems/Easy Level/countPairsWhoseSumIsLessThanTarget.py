# 2824.) Count Pairs Whose Sum is Less than Target
# Categories: Array, Two Pointers, Binary Search, Sorting

class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        pairs = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i < j) and (nums[i] + nums[j] < target):
                    pairs.append(tuple([nums[i], nums[j]]))        
    
        return len(pairs)
