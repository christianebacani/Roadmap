# 349.) Intersection of Two Arrays
# Categories: Array, Hash Table, Two Pointers, Binary Search, Sorting

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                result.append(nums1[i])
        
        return list(set(result))