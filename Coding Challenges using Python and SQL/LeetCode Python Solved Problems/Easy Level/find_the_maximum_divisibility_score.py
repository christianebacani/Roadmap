# 2644.) Find the Maximum Divisibility Score
# Categories: Array

class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        maximum_divisible_score = 0

        for i in range(len(divisors)):
            divisible_score = 0
    
            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    divisible_score += 1
            
            if divisible_score > maximum_divisible_score:
                maximum_divisible_score = divisible_score
        
        divisors_with_maximum_divisible_scores = []

        for i in range(len(divisors)):
            divisible_score = 0

            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    divisible_score += 1
            
            if divisible_score == maximum_divisible_score:
                divisors_with_maximum_divisible_scores.append(divisors[i])
        
        return min(divisors_with_maximum_divisible_scores)