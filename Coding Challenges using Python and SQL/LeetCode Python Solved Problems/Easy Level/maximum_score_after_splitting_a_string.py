# 1422.) Maximum Score After Splitting a String
# Categories: String, Prefix Sum

class Solution:
    def maxScore(self, s: str) -> int:
        scores = []

        for i in range(len(s) - 1):
            left_substring = s[:i + 1]
            right_substring = s[i + 1:]

            scores.append(left_substring.count('0') + right_substring.count('1'))
        
        return max(scores)