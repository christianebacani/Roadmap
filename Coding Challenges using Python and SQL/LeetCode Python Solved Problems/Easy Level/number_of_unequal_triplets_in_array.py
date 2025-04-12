# 2475.) Number of Unequal Triplets in Array
# Categories: Array, Hash Table, Sorting

class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        triplets = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (i < j) and (j < k) and (len(set([nums[i], nums[j], nums[k]])) == 3):
                        triplets.append(tuple([i, j, k]))

        return len(triplets)
