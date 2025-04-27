# 389.) Find the Difference
# Categories: Hash Table, String, Bit Manipulation, Sorting

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(len(t)):
            if t[i] not in s or t.count(t[i]) > s.count(t[i]):
                return t[i]