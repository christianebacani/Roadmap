# 3289.) The Two Sneaky Numbers of Digitville
# Categories : Array, Hash Table, Math

class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        distinct_nums = list(set(nums))
        sneaky_numbers = []

        for distinct_num in distinct_nums:
            count = 0
    
            for num in nums:
                if distinct_num == num:
                    count += 1

            if count > 1:
                sneaky_numbers.append(distinct_num)

        return sneaky_numbers