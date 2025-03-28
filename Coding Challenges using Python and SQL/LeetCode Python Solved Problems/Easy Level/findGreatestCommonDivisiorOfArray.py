# 1979.) Find Greatest Common Divisor of Array
# Categories: Array, Math, Number Theory

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        common_divisors = []

        for i in range(1, max_num + 1):
            if (min_num % i == 0) and (max_num % i == 0):
                common_divisors.append(i)
        
        return max(common_divisors)
