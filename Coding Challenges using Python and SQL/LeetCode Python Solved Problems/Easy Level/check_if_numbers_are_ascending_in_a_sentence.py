# 2042.) Check if Numbers Are Ascending in a Sentence
# Categories: String

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        numbers = []
        
        for i in range(len(s)):
            if s[i].isdigit():
                numbers.append(int(s[i]))

        for i in range(1, len(numbers)):
            if numbers[i - 1] >= numbers[i]:
                return False

        return True
