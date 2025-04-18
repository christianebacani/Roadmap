# 2243.) Calculate Digit Sum of a String
# Categories: String, Simulation

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            sum_digits = ''

            for i in range(0, len(s), k):
                sum = 0

                for j in range(len(s[i:i + k])):
                    sum += int(s[i:i + k][j])

                sum_digits += str(sum)

            s = sum_digits

        return s