# 1624.) Largest Substring Between Two Equal Characters
# Categories: Hash Table, String

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        substrings = []
    
        for i in range(len(s)):
            for j in range(len(s)):
                if i < j and s[i] == s[j]:
                    substrings.append(len(s[i + 1:j]))
        
        return max(substrings, default=-1)