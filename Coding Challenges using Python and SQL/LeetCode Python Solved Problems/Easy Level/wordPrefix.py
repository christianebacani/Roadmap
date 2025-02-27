# 1455.) Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Category : Two Pointers, String, String Matching

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentenceList = str(sentence).split(' ')

        for index, word in enumerate(sentenceList):
            if word.startswith(searchWord):
                return index + 1
        
        return -1

