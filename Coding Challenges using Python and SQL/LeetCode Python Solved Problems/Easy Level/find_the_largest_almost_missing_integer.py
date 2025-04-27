# 3471.) Find the Largest Almost Missing Integer
# Categories: Array, Hash Table

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        subarray_of_length_k = []

        for i in range(len(nums)):
            subarray = nums[i : i + k]

            if len(subarray) != k:
                continue
            
            subarray_of_length_k.append(subarray)
        
        frequency_of_every_element_in_subarrays = {}

        for i in range(len(nums)):
            frequency = 0

            for j in range(len(subarray_of_length_k)):
                if nums[i] in subarray_of_length_k[j]:
                    frequency += 1
            
            frequency_of_every_element_in_subarrays[nums[i]] = frequency
        
        elements_that_appears_once_in_every_subarray = []

        for element, frequency in frequency_of_every_element_in_subarrays.items():
            if frequency == 1:
                elements_that_appears_once_in_every_subarray.append(element)
        
        return max(elements_that_appears_once_in_every_subarray, default=-1)