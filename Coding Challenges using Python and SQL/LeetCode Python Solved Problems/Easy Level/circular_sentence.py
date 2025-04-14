# 2490.) Circular Sentence
# Categories: String

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        first_and_last_characters = []

        for i in range(len(sentence)):
            first_and_last_characters.append([sentence[i][0], sentence[i][-1]])

        last_index = len(first_and_last_characters) - 1

        for i in range(len(first_and_last_characters)):
            if (i != last_index) and (first_and_last_characters[i][1] != first_and_last_characters[i + 1][0]):
                return False
            
            elif (i == last_index) and (first_and_last_characters[i][1] != first_and_last_characters[0][0]):
                return False
        
        return True