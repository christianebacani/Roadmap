# 1413.) Minimum Value to Get Positive Step by Step Sum
# Categories: Array, Prefix Sum

class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        start_values = []

        for i in range(1, 5000 + 1):
            step_by_step_sum_less_than_1 = False
            sum = i
            
            for j in range(len(nums)):
                sum += nums[j]

                if sum < 1:
                    step_by_step_sum_less_than_1 = True
                    break

            if not step_by_step_sum_less_than_1:
                start_values.append(i)
        
        return min(start_values)