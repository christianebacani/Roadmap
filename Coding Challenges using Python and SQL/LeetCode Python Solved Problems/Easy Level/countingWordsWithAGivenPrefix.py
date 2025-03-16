# 2185.) Counting Words With a Given Prefix
# Categories: Array, String, String Matching

class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0

        for i in range(len(words)):
            if words[i].startswith(pref):
                count += 1
    
        return count
