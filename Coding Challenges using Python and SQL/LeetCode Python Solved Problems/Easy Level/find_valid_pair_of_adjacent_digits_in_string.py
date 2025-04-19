# 3438.) Find Valid Pair of Adjacent Digits in String
# Categories: Hash Table, String, Counting

class Solution:
    def findValidPair(self, s: str) -> str:
        valid_adjacent_pairs = []

        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                continue

            if (s.count(s[i - 1]) == int(s[i - 1])) and (s.count(s[i]) == int(s[i])):
                valid_adjacent_pairs.append(s[i - 1] + s[i])

        if valid_adjacent_pairs == []:
            return ''
        
        return valid_adjacent_pairs[0]