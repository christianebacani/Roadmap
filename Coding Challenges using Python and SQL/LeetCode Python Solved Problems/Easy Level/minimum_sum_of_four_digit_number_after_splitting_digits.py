# 2160.) Minimum Sum of Four Digit Number After Splitting Digits
# Categories: Math, Greedy, Sorting

class Solution:
    def minimumSum(self, num: int) -> int:
        num_str = str(num)
        digits = []
        
        for i in range(len(num_str)):
            digits.append(int(num_str[i]))

        first_digits = ''
        second_digits = ''

        digits = sorted(digits)
        
        first_digits += str(digits[0])
        first_digits += str(digits[2])

        second_digits += str(digits[1])
        second_digits += str(digits[3])

        return int(first_digits) + int(second_digits)