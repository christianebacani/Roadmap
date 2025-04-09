# 2255.) Count Prefixes of a Given String
# Categories: Array, String

class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        count = 0
        
        for i in range(len(words)):
            if s.startswith(words[i]):
                count += 1
        
        return count