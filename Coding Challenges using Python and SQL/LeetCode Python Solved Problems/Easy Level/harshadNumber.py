# 3099.) Harshad Number
# Categories: Math

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x = str(x)
        digit_sum = 0
        
        for digit in x:
            digit_sum += int(digit)

        if int(x) % digit_sum == 0:
            return digit_sum
        
        return -1
