# 2828.) Check if a String Is an Acronym of Words
# Categories: Array, String

class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        words_acronym = ''
        
        for i in range(len(words)):
            words_acronym += words[i][0]
        
        if words_acronym == s:
            return True
        
        return False