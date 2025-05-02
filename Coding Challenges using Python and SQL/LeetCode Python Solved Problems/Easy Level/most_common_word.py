# 819.) Most Common Word
# Categories: Array, Hash Table, String, Counting

from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = '!?\',;.'

        for i in range(len(symbols)):
            paragraph = paragraph.replace(symbols[i], ' ')
        
        paragraph = paragraph.split()
        
        for i in range(len(paragraph)):
            paragraph[i] = paragraph[i].lower()
        
        not_banned_words_and_frequencies = {}

        for i in range(len(paragraph)):
            if paragraph[i] not in banned:
                not_banned_words_and_frequencies[paragraph[i]] = paragraph.count(paragraph[i])
        
        maximum_frequency = max(list(not_banned_words_and_frequencies.values()))

        for word, frequency in not_banned_words_and_frequencies.items():
            if maximum_frequency == frequency:
                return word