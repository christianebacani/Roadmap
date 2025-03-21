# 1967.) Number of Strings that Appear as Substrings in Word
# Categories: Array, String

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        
        for i in range(len(patterns)):
            if patterns[i] in word:
                count += 1
        
        return count
    