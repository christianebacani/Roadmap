# 3423.) Maximum Difference Between Adjacent Elements in a Circular Array
# Categories: Array

class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        nums.insert(0, nums[-1])
        nums.append(nums[1])
        absolute_differences = []

        for i in range(1, len(nums) - 1):
            absolute_differences.append(abs(nums[i] - nums[i - 1]))
            absolute_differences.append(abs(nums[i] - nums[i + 1]))

        return max(absolute_differences)
