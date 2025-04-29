# 2748.) Number of Beautiful Pairs
# Categories: Array, Hash Table, Math, Counting, Number Theory

from typing import List

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(x: int, y: int) -> int:
            if x >= y:
                maximum_number = x

            else:
                maximum_number = y

            divisors = []

            for divisor in range(1, maximum_number + 1):
                if x % divisor == 0 and y % divisor == 0:
                    divisors.append(divisor)

            return max(divisors)
    
        number_of_beautiful_pairs = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                first_digit_of_nums_i = int(str(nums[i])[0])
                last_digit_of_nums_j = int(str(nums[j])[-1])

                if i < j and gcd(first_digit_of_nums_i, last_digit_of_nums_j) == 1:
                    number_of_beautiful_pairs += 1
        
        return number_of_beautiful_pairs
