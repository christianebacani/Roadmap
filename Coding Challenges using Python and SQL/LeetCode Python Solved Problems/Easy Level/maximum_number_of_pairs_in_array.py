# 2341.) Maximum Number of Pairs in Array
# Categories: Array, Hash Table, Counting

class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        frequencies = {}
        
        for i in range(len(nums)):
            frequency = 0

            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    frequency += 1
        
            frequencies[nums[i]] = frequency
        
        pairs = 0
        leftovers = 0
        
        for _, frequency in frequencies.items():
            if frequency % 2 == 0:
                pairs += frequency // 2
        
            else:
                pairs += (frequency - 1) // 2
                leftovers += 1
        
        return [pairs, leftovers]
        