# 1512.) Number of Good Pairs
# Categories : Array, Hash Table, Math, Counting

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        good_pairs = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] == nums[j]) and (i < j) and (tuple([i, j]) not in good_pairs):
                    good_pairs.append(tuple([i, j]))
    
        return len(good_pairs)

                            