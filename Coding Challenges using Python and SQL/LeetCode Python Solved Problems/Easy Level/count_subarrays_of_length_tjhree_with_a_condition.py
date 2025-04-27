# 3392.) Count Subarrays of Length Three With a Condtion
# Categories: Array

class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        count = 0

        for i in range(len(nums)):
            subarray = nums[i : i + 3]
            
            if len(subarray) != 3:
                continue

            sum_of_first_and_third_number = subarray[0] + subarray[2]
            
            if sum_of_first_and_third_number * 2 == subarray[1]:
                count += 1
        
        return count