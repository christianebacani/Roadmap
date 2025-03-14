# 3194.) Minimum Average of Smallest and Largest Elements
# Categories: Array, Two Pointers, Sorting

class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        averages = []

        while len(nums) > 1:
            minimum_element = min(nums)
            maximum_element = max(nums)
            averages.append((minimum_element + maximum_element) / 2)

            nums.remove(minimum_element)
            nums.remove(maximum_element)
    
        if isinstance(min(averages), int):
            return float(min(averages))

        return round(min(averages), 1)
