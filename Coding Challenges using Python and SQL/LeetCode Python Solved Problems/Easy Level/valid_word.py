# 3136.) Valid Word
# Categories: String

class Solution:
    def isValid(self, word: str) -> bool:
        def isWordLengthMinOf3Chars(word: str) -> bool:
            if len(word) >= 3:
                return True
            
            return False

        def isWordOnlyContainsAlnum(word: str) -> bool:
            for i in range(len(word)):
                if not word[i].isalnum():
                    return False
            
            return True
        
        def isWordContainsAtleastOneVowel(word: str) -> bool:
            vowels = ['a', 'e', 'i', 'o', 'u']

            for i in range(len(word)):
                if word[i].lower() in vowels:
                    return True
            
            return False
        
        def isWordContainsAtleastOneConsonant(word: str) -> bool:
            vowels = ['a', 'e', 'i', 'o', 'u']

            for i in range(len(word)):
                if word[i].lower().isalpha() and word[i].lower() not in vowels:
                    return True
            
            return False


        if isWordLengthMinOf3Chars(word) and isWordOnlyContainsAlnum(word) and isWordContainsAtleastOneVowel(word) and isWordContainsAtleastOneConsonant(word):
            return True
        
        return False