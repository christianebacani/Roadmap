# 2553.) Separate the Digits in an Array
# Categories: Array, Simulation

class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        answer = []
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
            for j in range(len(nums[i])):
                answer.append(int(nums[i][j]))

        return answer