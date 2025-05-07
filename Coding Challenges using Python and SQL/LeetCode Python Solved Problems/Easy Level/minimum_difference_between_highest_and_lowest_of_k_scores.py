# 1984.) Minimum Difference Between Highest and Lowest of K Scores
# Categories: Array, Sliding Window, Sorting

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        differences_of_max_and_min_k_scores = []

        for i in range(len(nums)):
            k_scores = nums[i : i + k]

            if len(k_scores) != k:
                continue

            differences_of_max_and_min_k_scores.append(max(k_scores) - min(k_scores))

        return min(differences_of_max_and_min_k_scores)