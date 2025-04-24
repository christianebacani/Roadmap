# 2455.) Average Value of Even Numbers That Are Divisible by Three
# Categories: Array, Math

import math

class Solution:
    def averageValue(self, nums: list[int]) -> int:
        even_number_that_is_divisible_by_three = []

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                continue

            if nums[i] % 3 == 0:
                even_number_that_is_divisible_by_three.append(nums[i])

        if len(even_number_that_is_divisible_by_three) == 0:
            return 0
        
        return math.floor(sum(even_number_that_is_divisible_by_three) / len(even_number_that_is_divisible_by_three))