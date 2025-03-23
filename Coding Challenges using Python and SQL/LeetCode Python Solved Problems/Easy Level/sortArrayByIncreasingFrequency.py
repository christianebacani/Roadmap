# 1636.) Sort Array by Increasing Frequency
# Categories: Array, Hash Table, Sorting

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        element_and_frequency = {}

        for i in range(len(nums)):
            frequency = 0

            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    frequency += 1
            
            element_and_frequency[nums[i]] = frequency

        sorted_frequencies = sorted(list(set(element_and_frequency.values())))
        result = []
    
        for sorted_frequency in sorted_frequencies:
            elements = []

            for element, frequency in element_and_frequency.items():
                if sorted_frequency == frequency:
                    for _ in range(frequency):
                        elements.append(element)

            result.extend(sorted(elements, reverse=True))
      
        return result
