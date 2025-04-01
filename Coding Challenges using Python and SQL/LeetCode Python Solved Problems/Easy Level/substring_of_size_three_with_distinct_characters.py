# 1876.) Substring of Size Three with Distinct Characters
# Categories: Hash Table, String, Sliding Window, Counting

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        substrings = []
    
        for i in range(len(s)):
            substring = s[i:i + 3]

            if len(substring) == 3:
                substrings.append(substring)
        
        count = 0
        
        for i in range(len(substrings)):
            distinct_substring = set(substrings[i])
            
            if len(distinct_substring) == 3:
                count += 1
        
        return count