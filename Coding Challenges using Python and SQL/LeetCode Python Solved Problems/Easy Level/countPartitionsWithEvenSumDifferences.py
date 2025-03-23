# 3232.) Count Partitions with Even Sum Difference
# Categories: Array, Math, Prefix Sum

class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        number_of_partitions = 0

        for i in range(len(nums)):
            left_subarray = nums[0:i + 1]
            right_subarray = nums[i + 1: len(nums)]
            
            if (left_subarray != [] and right_subarray != []) and ((sum(left_subarray) - sum(right_subarray)) % 2 == 0):
                number_of_partitions += 1

        return number_of_partitions
            