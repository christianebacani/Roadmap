# 3131.) Find the Integer Added to Array I
# Categories: Array

from typing import List

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        if nums1[0] > nums2[0]:
            return abs(nums1[0] - nums2[0]) * -1
            
        elif nums1[0] < nums2[0]:
            return abs(nums1[0] - nums2[0])
        
        else:
            return 0