# 2974.) Minimum Number Game
# Categories: Array, Sorting, Heap(Priority Queue), Simulation

class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        arr = []
    
        for i in range(0, len(nums), 2):
            sub_arr = []
            sub_arr.extend([nums[i], nums[i + 1]])
        
            sub_arr = sorted(sub_arr, reverse=True)
            arr.extend(sub_arr)

        return arr
