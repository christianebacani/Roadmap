# 2544.) Alternating Digit Sum
# Categories: Math

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        alternate_digits = []

        for i in range(len(n)):
            if i % 2 == 0:
                alternate_digits.append(int(n[i]))
            
            else:
                alternate_digits.append(int(n[i]) * -1)

        return sum(alternate_digits)