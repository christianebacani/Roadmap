# 922.) Sort Array By Parity II
# Categories: Array, Two Pointers, Sorting

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even_elements = []
        odd_elements = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_elements.append(nums[i])
            
            else:
                odd_elements.append(nums[i])
        
        if len(even_elements) >= len(odd_elements):
            number_of_elements = len(even_elements)
        
        else:
            number_of_elements = len(odd_elements)

        sorted_by_parity = []

        for i in range(number_of_elements):
            try:
                sorted_by_parity.append(even_elements[i])
            
            except IndexError:
                pass

            try:
                sorted_by_parity.append(odd_elements[i])
            
            except IndexError:
                pass
        
        return sorted_by_parity