# 28.) Find the Index of the First Occurence in a String
# Categories: Two Pointers, String, String Matching

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            substring = haystack[i : i + len(needle)]
            
            if substring == needle:
                return i
        
        return -1