# 1935.) Maximum Number of Words You Can Type
# Categories: Hash Table, String

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        brokenLetters = list(brokenLetters)
        count = 0

        for i in range(len(text)):
            contains_broken_letter = False

            for j in range(len(brokenLetters)):
                if brokenLetters[j] in text[i]:
                    contains_broken_letter = True
            
            if not contains_broken_letter:
                count += 1
        
        return count
