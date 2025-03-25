# a2176.) Count Equal and Divisible Pairs in an Array
# Categories: Array

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        pairs = []
    
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i < j) and (nums[i] == nums[j]) and ((i * j) % k == 0):
                    pairs.append(tuple([nums[i], nums[j]]))
    
        return len(pairs)