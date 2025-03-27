# 1748.) Sum of Unique Elements
# Categories: Array, Hash Table, Counting

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        unique_elements = []
        
        for i in range(len(nums)):
            appearance_count = 0
            
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    appearance_count += 1
            
            if appearance_count == 1:
                unique_elements.append(nums[i])
    
        return sum(unique_elements)
