# 258.) Add Digits
# Categories: Math, Simulation, Number Theory

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = str(num)
            sum = 0

            for i in range(len(num)):
                sum += int(num[i])
            
            num = sum
        
        return num

            