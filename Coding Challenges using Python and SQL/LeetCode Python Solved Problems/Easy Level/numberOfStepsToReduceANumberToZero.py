# 1342.) Number of Steps to Reduce a Number to Zero
# Categories: Math, Bit Manipulation

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        while True:
            if num == 0:
                return count

            if num % 2 == 0:
                num = num / 2
                count += 1

            else:
                num = num - 1
                count += 1
        
            
