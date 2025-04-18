# 520.) Detect Capital
# Categories: String

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if (word.isupper()) or (word.islower()):
            return True

        if word[0].islower():
            return False
        
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
        
        return True