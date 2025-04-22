# 1078.) Occurences After Bigram
# Categories: String

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        text = text.split()
        third_words = []

        for i in range(len(text)):
            first_and_second_word = ' '.join(text[i : i + 2])

            try:
                if first_and_second_word == first + ' ' + second:
                    third_words.append(text[i + 2])

            except IndexError:
                pass
            
        return third_words