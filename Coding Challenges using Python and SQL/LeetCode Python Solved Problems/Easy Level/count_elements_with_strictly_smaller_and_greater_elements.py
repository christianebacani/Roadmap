# 2148.) Count Elements With Strictly Smaller and Greater Elements
# Categories: Array, Sorting, Counting

from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        elements = []
        
        for i in range(len(nums)):
            num_of_elements_that_is_strictly_greater_than_current_element = 0
            num_of_elements_that_is_strictly_less_than_current_element = 0

            for j in range(len(nums)):
                if i == j:
                    continue

                if nums[i] > nums[j]:
                    num_of_elements_that_is_strictly_greater_than_current_element += 1
                
                elif nums[i] < nums[j]:
                    num_of_elements_that_is_strictly_less_than_current_element += 1
            
            if num_of_elements_that_is_strictly_greater_than_current_element >= 1 and num_of_elements_that_is_strictly_less_than_current_element >= 1:
                elements.append(nums[i])
        
        return len(elements)