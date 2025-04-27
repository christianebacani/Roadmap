# 2351.) First Letter to Appear Twice
# Categories: Hash Table, String, Bit Manipulation, Counting

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] not in stack:
                stack.append(s[i])
                continue

            return s[i]