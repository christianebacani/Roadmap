# 58.) Length of Last Word
# Categories: String

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()[::-1]
        last_word = s[0].strip()

        return len(last_word)