# 3264.) Final Array State After K Multiplication Operations I
# Categories: Array, Math, Heap (Priority Queue), Simulation

class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        number_of_operations = k
    
        for _ in range(number_of_operations):
            minimum_num = min(nums)

            for index, num in enumerate(nums):
                if minimum_num == num:
                    index = index
                    break
        
            nums[index] = minimum_num * multiplier
    
        return nums
