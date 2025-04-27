# 2873.) Maximum Value of an Ordered Triplet I
# Categories: Array

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        triplets_value = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i < j < k and ((nums[i] - nums[j]) * nums[k]) >= 0:
                        triplets_value.append((nums[i] - nums[j]) * nums[k])
                    
                    elif i < j < k and ((nums[i] - nums[j]) * nums[k]) < 0:
                        triplets_value.append(0)
        
        return max(triplets_value)