# 2200.) Find All K-Distant Indices in an Array
# Categories: Array, Two Pointers

class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        k_distant_indices = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] != key:
                    continue

                if abs(i - j) <= k:
                    k_distant_indices.append(i)
                    break
        
        k_distant_indices = sorted(k_distant_indices)

        return k_distant_indices