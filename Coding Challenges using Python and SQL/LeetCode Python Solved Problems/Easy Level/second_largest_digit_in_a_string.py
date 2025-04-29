# 1896.) Second Largest Digit in a String
# Categories: Hash Table, String

class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []

        for i in range(len(s)):
            if s[i].isdigit():
                digits.append(int(s[i]))
        
        digits = sorted(list(set(digits)), reverse=True)

        if len(digits) <= 1:
            return -1
        
        return digits[1]