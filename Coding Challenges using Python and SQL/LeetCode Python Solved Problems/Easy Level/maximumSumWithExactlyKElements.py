# 2656.) Maximum Sum With Exactly K Elements
# Categories: Array, Greedy

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        sorted_distinct_nums = sorted(list(set(nums)), reverse=True)
        maximum_number = sorted_distinct_nums[0]

        sum = 0
        
        for i in range(k):
            sum += maximum_number
            maximum_number += 1
        
        return sum
