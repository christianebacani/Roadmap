# 169.) Majority Element
# Categories: Array, Hash Table, Divide and Conquer, Sorting, Counting

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        frequencies = {}
        distinct_nums = list(set(nums))

        for i in range(len(distinct_nums)):
            frequencies[distinct_nums[i]] = nums.count(distinct_nums[i])
        
        majority_count = max(list(frequencies.values()))
        
        for number, frequency in frequencies.items():
            if frequency == majority_count:
                return number