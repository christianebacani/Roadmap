# 242.) Valid Anagram
# Categories: Hash Table, String, Sorting

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        distinct_characters = list(set(s + t))

        for i in range(len(distinct_characters)):
            if s.count(distinct_characters[i]) != t.count(distinct_characters[i]):
                return False
        
        return True