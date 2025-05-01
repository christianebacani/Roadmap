# 2748.) Check if Array is Good
# Categories: Array, Hash Table, Sorting

from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        permutation_of_base_n = []

        for i in range(1, n + 1):
            permutation_of_base_n.append(i)

            if i == n:
                permutation_of_base_n.append(i)
        
        permutation_of_base_n = sorted(permutation_of_base_n)

        if sorted(nums) == permutation_of_base_n:
            return True
        
        return False