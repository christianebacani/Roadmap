# 3467.) Transform Array by Parity
# Categories : Array, Sorting, Counting

class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        results = [0 if num % 2 == 0 else 1 for num in nums]
        results = sorted(results)
    
        return results
