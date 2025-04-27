# 2465.) Number of Distinct Averages
# Categories: Array, Hash Table, Two Pointers, Sorting

from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = []

        while nums != []:
            nums = sorted(nums)
            minimum_number = nums[0]
            maximum_number = nums[-1]
            
            averages.append(round((minimum_number + maximum_number) / 2, 1))
            nums.remove(minimum_number)
            nums.remove(maximum_number)
        
        return len(set(averages))