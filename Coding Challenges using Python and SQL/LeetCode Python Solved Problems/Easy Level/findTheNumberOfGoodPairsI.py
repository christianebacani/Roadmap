# 3162.) Find the Number of Good Pairs I
# Categories: Array, Hash Table

class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        good_pairs = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    good_pairs.append(tuple([nums1[i], nums2[j]]))
    
        return len(good_pairs)
