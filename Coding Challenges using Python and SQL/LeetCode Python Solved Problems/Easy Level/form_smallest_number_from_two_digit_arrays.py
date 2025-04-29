# 2605.) Form Smallest Number From Two Digit Arrays
# Categories: Array, Hash Table, Enumeration

from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                return nums1[i]

        minimum_num1 = min(nums1)
        minimum_num2 = min(nums2)

        numbers = []

        for i in range(len(nums1)):
            if minimum_num1 == nums1[i]:
                numbers.append(str(nums1[i]))
        
        for i in range(len(nums2)):
            if minimum_num2 == nums2[i]:
                numbers.append(str(nums2[i]))
        
        numbers = int(''.join(sorted(numbers)))

        return numbers