# 2068.) Check Whether Two Strings are Almost Equivalent
# Categories: Hash Table, String, Counting

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for i in range(len(word1)):
            if abs(word1.count(word1[i]) - word2.count(word1[i])) > 3:
                return False
        
        for i in range(len(word2)):
            if abs(word2.count(word2[i]) - word1.count(word2[i])) > 3:
                return False

        return True