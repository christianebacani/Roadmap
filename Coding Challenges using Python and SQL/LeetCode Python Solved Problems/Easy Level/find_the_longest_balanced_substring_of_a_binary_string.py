# 2609.) Find the Longest Balanced Substring of a Binary String
# Categories: String

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        def isBinaryStringIfBalance(binary_str: str) -> bool:
            index_delimiter = binary_str.count('0')
            
            if set(binary_str[:index_delimiter]) != {'0'}:
                return False
            
            if binary_str.count('0') != binary_str.count('1'):
                return False
            
            return True
    
        balanced_substring_lengths = []

        for i in range(1, len(s) + 1):
            for j in range(len(s)):
                substring = s[j : j + i]

                if isBinaryStringIfBalance(substring) is True:
                    balanced_substring_lengths.append(len(substring))

        return max(balanced_substring_lengths, default=0)