# 3083.) Existence of a Substring in a String and Its Reverse
# Categories: Hash Table, String

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        substring_present = []

        for i in range(1, len(s)):
            substring = s[i - 1] + s[i]

            if len(substring) != 2:
                continue

            if substring in s[::-1]:
                substring_present.append(substring)
        
        if substring_present == []:
            return False
        
        return True