# 3550.) Smallest Index With Digit Sum Equal to Index
# Categories: Array, Math

class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        smallest_index = -1

        for i in range(len(nums)):
            sum_of_its_digits = 0

            for j in range(len(str(nums[i]))):
                sum_of_its_digits += int(str(nums[i])[j])

            if sum_of_its_digits == i:
                smallest_index = i
                break
        
        return smallest_index