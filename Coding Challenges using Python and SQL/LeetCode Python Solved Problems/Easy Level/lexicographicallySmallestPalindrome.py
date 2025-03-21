# 2697.) Lexicographically Smallest Palindrome
# Categories: Two Pointers, String, Greedy

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        
        for i in range(len(s)):
            if s[i] == s[len(s) - i - 1]:
                continue

            if s[i] > s[len(s) - i - 1]:
                s[i] = s[len(s) - i - 1]
                
            elif s[len(s) - i - 1] > s[i]:
                s[len(s) - i - 1] = s[i]

        return ''.join(s)
