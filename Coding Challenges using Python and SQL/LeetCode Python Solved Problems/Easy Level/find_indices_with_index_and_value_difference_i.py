# 2903.) Find Indices With Index and Value Difference I
# Categories: Array, Two Pointers

class Solution:
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        
        return [-1, -1]