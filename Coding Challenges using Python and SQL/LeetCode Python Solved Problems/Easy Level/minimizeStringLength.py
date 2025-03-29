# 2716.) Minimize String Length
# Categories: Hash Table, String

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s = list(set(list(s)))

        return len(s)
    