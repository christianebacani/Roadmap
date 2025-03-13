# 1816.) Truncate Sentence
# Categories: Array, String

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        s = ' '.join(s[:k])

        return s
