# 1848.) Minimum Distance to the Target Element
# Categories: Array

from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        distances = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                distances.append(abs(i - start))
        
        return min(distances)