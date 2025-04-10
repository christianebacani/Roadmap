# 3069.) Distribute Elements Into Two Arrays I
# Categories: Array, Simulation

class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr1 = []
        arr2 = []
    
        for i in range(n):
            if i == 0:
                arr1.append(nums[i])
            
            elif i == 1:
                arr2.append(nums[i])
            
            elif arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            
            else:
                arr2.append(nums[i])
        
        return arr1 + arr2