# 2367. Number of Arithmetic Triplets
# Categories: Array, Hash Table, Two Pointers, Enumeration

class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        arithmetic_triplets = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                        triplets = [nums[i], nums[j], nums[k]]
                        triplets = sorted(triplets)
                        arithmetic_triplets.append(tuple(triplets))
    
        return len(arithmetic_triplets)
