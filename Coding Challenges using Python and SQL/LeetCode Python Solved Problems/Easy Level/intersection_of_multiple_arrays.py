# 2248.) Intersection of Multiple Arrays
# Categories: Array, Hash Table, Sorting, Counting

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        elements = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] not in elements:
                    elements.append(nums[i][j])
        
        result = []

        for i in range(len(elements)):
            present_in_each_array = True

            for j in range(len(nums)):
                if elements[i] not in nums[j]:
                    present_in_each_array = False
                    break
            
            if present_in_each_array:
                result.append(elements[i])

        result = sorted(result)
        return result