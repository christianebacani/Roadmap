# 2932.) Maximum Strong Pair XOR I
# Categories: Array, Hash Table, Bit Manipulation, Trie, Sliding Window

class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        strong_pairs = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) <= min([nums[i], nums[j]]):
                    strong_pairs.append(tuple([nums[i], nums[j]]))
        
        xors = []
        
        for i in range(len(strong_pairs)):
            xors.append(strong_pairs[i][0] ^ strong_pairs[i][1])
        
        return max(xors)
