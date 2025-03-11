# 2574.) Left and Right Sum Differences
# Categories: Array, Prefix Sum

class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left_sum = []
        right_sum = []
        answer = []

        for i in range(len(nums)):
            try:
                left_side_sum = sum(nums[:i])
                right_side_sum = sum(nums[i + 1:])
                left_sum.append(left_side_sum)
                right_sum.append(right_side_sum)

            except IndexError:
                break
    
        for i in range(len(left_sum)):
            answer.append(abs(left_sum[i] - right_sum[i]))
    
        return answer
