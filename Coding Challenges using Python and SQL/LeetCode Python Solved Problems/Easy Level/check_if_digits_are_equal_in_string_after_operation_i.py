# 3461.) Check if Digits Are Equal in String After Operations I
# Categories: Easy

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            result = ''

            for i in range(1, len(s)):
                previous_digit = s[i - 1]
                current_digit = s[i]

                result += str((int(previous_digit) + int(current_digit)) % 10)

            s = result

        if s[0] == s[1]:
            return True
        
        return False