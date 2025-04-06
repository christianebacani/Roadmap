# 2180.) Count Integers With Even Digit Sum
# Categories: Math, Simulation

class Solution:
    def countEven(self, num: int) -> int:
        positive_integers = []

        for i in range(1, num + 1):
            number = str(i)
            sum = 0

            for j in range(len(number)):
                sum += int(number[j])

            if sum % 2 == 0:
                positive_integers.append(sum)

        return len(positive_integers)
         