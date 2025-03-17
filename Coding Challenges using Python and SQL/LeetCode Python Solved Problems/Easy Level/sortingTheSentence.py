# 1859.) Sorting the Sentence
# Categories: String, Sorting

class Solution:
    def sortSentence(self, s: str) -> str:
        reconstructed_sentence = []
        s = s.split()

        for i in range(len(s)):
            i += 1

            for j in range(len(s)):
                if i == int(s[j][-1]):
                    reconstructed_sentence.append(s[j][:-1])
    
        reconstructed_sentence = ' '.join(reconstructed_sentence)

        return reconstructed_sentence  
