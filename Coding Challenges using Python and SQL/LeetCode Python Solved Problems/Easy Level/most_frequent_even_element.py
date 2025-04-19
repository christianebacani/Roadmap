# 2404.) Most Frequent Even Element
# Categories: Array, Hash Table, Counting

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        distinct_sorted_nums = sorted(list(set(nums)))
        even_element_frequencies = {}
        
        for i in range(len(distinct_sorted_nums)):
            if distinct_sorted_nums[i] % 2 != 0:
                continue

            even_element_frequencies[distinct_sorted_nums[i]] = nums.count(distinct_sorted_nums[i])

        if even_element_frequencies == {}:
            return -1
    
        maximum_frequency = max(list(even_element_frequencies.values()))

        for element, frequency in even_element_frequencies.items():
            if maximum_frequency == frequency:
                return element