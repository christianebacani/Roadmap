# 2154.) Keep Multiplying Found Values by Two
# Categories: Array, Hash Table, Sorting, Simulation

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while original in nums:
            original = original * 2
        
        return original