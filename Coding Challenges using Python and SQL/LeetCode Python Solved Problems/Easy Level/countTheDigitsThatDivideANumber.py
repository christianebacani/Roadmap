# 2520.) Count the Digits That Divide a Number
# Categories: Math

class Solution:
    def countDigits(self, num: int) -> int:
        num = str(num)
        count = 0 

        for digit in num:
            digit = int(digit)

            if int(num) % digit == 0:
                count += 1

        return count
