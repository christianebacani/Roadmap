# 2164.) Sort Even and Odd Indices Independently
# Categories: Array, Sorting

class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        even_index_elements = []
        odd_index_elements = []

        for i in range(len(nums)):
            if i % 2 == 0:
                even_index_elements.append(nums[i])
            
            else:
                odd_index_elements.append(nums[i])

        even_index_elements = sorted(even_index_elements)
        odd_index_elements = sorted(odd_index_elements, reverse=True)

        if len(even_index_elements) >= len(odd_index_elements):
            number_of_elements = len(even_index_elements)
        
        else:
            number_of_elements = len(odd_index_elements)
        
        arranged_nums = []

        for i in range(number_of_elements):
            try:
                arranged_nums.append(even_index_elements[i])

            except IndexError:
                pass

            try:
                arranged_nums.append(odd_index_elements[i])

            except IndexError:
                pass
        
        return arranged_nums