# 2016.) Maximum Difference Between Increasing Elements
# Categories: Array

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        maximum_differences = []

        for i in range(len(nums)):
            differences = []

            for j in range(len(nums)):
                if i < j and nums[i] < nums[j]:
                    differences.append(abs(nums[i] - nums[j]))

            if differences != []:
                maximum_differences.append(max(differences))

        return max(maximum_differences, default=-1)