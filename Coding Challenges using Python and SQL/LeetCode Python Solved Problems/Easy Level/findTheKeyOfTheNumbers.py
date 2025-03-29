# 3270.) Find the Key of the Numbers
# Categories: Math

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [str(num1), str(num2), str(num3)]
        
        for index, num in enumerate(nums):
            if len(num) != 4:
                leading_zeros = (4 - len(num)) * '0'
                nums[index] = leading_zeros + num
        
        keys = []
        
        for i in range(len(nums[0])):
            key = []
            
            for j in range(len(nums)):
                key.append(int(nums[j][i]))
            
            keys.append(str(min(key)))
    

        keys = ''.join(keys).removeprefix('0')
        
        if keys == '':
            return 0
    
        return int(keys)
