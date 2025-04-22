# 2293.) Min Max Game
# Categories: Array, Simulation

class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
    
        while len(nums) != 1:
            newNums = []

            for i in range(0, len(nums), 2):
                newNums.append(nums[i : i + 2])

            nums = []

            for i in range(len(newNums)):
                if i % 2 == 0:
                    nums.append(min(newNums[i]))

                else:
                    nums.append(max(newNums[i]))

        return nums[0]