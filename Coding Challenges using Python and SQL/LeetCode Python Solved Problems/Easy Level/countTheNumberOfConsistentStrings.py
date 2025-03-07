# 1684.) Count the Number of Consistent Strings
# Categories : Array, Hash Table, String, Bit Manipulation, Counting

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed = [char for char in allowed]
        count = 0
    
        for word in words:
            allow = True

            for char in word:
                if char not in allowed:
                    allow = False
        
            if allow:
                count += 1
    
        return count
