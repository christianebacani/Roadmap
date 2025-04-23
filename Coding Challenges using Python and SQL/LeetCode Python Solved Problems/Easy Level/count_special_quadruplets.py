# 1995.) Count Special Quadruplets
# Categories: Array, Hash Table, Enumeration

class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        distinct_quadruplets = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    for l in range(len(nums)):
                        if i < j < k < l and nums[i] + nums[j] + nums[k] == nums[l]:
                            distinct_quadruplets.append(tuple([i, j, k, l]))
        
        return len(set(distinct_quadruplets))