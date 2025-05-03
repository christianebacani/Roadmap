# 434.) Number of Segments in a String
# Categories: String

class Solution:
    def countSegments(self, s: str) -> int:
        words = s.split()

        return len(words)