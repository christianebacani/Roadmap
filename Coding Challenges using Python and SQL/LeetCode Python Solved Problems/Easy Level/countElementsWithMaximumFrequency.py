# 3005.) Count Elements With Maximum Frequency
# Categories: Array, Hash Table, Counting

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        frequencies = {}
        
        for i in range(len(nums)):
            frequency = 0
            
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    frequency += 1
            
            frequencies[nums[i]] = frequency
        
        max_frequency = max(list(frequencies.values()), default=0)
        count = 0
        
        for i in range(len(nums)):
            frequency = 0
            
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    frequency += 1
            
            if max_frequency == frequency:
                count += 1
    
        return count
    