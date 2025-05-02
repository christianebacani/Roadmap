# 1805.) Number of Different Integers in a String
# Categories: Hash Table, String

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        formatted_word = ''

        for i in range(len(word)):
            if not word[i].isnumeric():
                formatted_word += ' '
            
            else:
                formatted_word += word[i]
        
        formatted_word = formatted_word.split()
        integers = []

        for i in range(len(formatted_word)):
            integers.append(int(formatted_word[i]))

        return len(set(integers))