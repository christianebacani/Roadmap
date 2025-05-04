# 2161.) Partition Array According to Given Pivot
# Categories: Array, Two Pointers, Simulation

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        elements_that_are_less_than_pivot = []
        elements_that_are_pivot = []
        elements_that_are_greater_than_pivot = []
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                elements_that_are_less_than_pivot.append(nums[i])
            
            elif nums[i] == pivot:
                elements_that_are_pivot.append(nums[i])
            
            else:
                elements_that_are_greater_than_pivot.append(nums[i])
        
        return elements_that_are_less_than_pivot + elements_that_are_pivot + elements_that_are_greater_than_pivot