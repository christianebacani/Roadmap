# 1365.) How Many Numbers Are Smaller Than the Current Number
# Categories: Array, Hash Table, Sorting, Counting Sort

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        answer = []

        for i in range(len(nums)):
            count = 0
    
            for j in range(len(nums)):
                if (nums[j] < nums[i]):
                    count += 1
    
            answer.append(count)

        return answer
