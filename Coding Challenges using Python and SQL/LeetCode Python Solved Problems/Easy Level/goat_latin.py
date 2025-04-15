# 824.) Goat Latin
# Categories: String

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()

        for i in range(len(sentence)):
            if sentence[i][0].lower() in ['a', 'e', 'i', 'o', 'u']:
                sentence[i] = sentence[i] + 'ma' + ((i + 1) * 'a')
            
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + 'ma' + ((i + 1) * 'a')

        return ' '.join(sentence)