# 2451.) Odd String Difference
# Categories: Array, Hash Table, String

class Solution:
    def oddString(self, words: list[str]) -> str:
        def getIntegerValOfLetter(char: str) -> int:
            alphabets = [
                'a', 'b', 'c', 'd',
                'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p',
                'q', 'r', 's', 't',
                'u', 'v', 'w', 'x',
                'y', 'z'
            ]
            
            return alphabets.index(char)

        word_differences = {}

        for i in range(len(words)):
            difference = []

            for j in range(1, len(words[i])):
                difference.append(getIntegerValOfLetter(words[i][j]) - getIntegerValOfLetter(words[i][j - 1]))

            word_differences[words[i]] = difference

        differences = list(word_differences.values())

        for word, difference in word_differences.items():
            if words.count(word) == 1 and differences.count(difference) == 1:
                return word