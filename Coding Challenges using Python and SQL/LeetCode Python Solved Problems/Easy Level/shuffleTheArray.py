# 1470.) Shuffle the Array
# Categories : Array

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        first_nums = nums[:n]
        second_nums = nums[n:]
        result_nums = []

        for index_first_num, first_num in enumerate(first_nums):
            for index_second_num, second_num in enumerate(second_nums):
                if index_first_num == index_second_num:
                    result_nums.append(first_num)
                    result_nums.append(second_num)
                    break
    
        return result_nums