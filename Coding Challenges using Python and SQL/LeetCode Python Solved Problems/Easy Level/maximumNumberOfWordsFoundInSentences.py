# 2114.) Maximum Number of Words Found in Sentences
# Categories: Array, String

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        counts = []

        for sentence in sentences:
            sentence = sentence.split()
            counts.append(len(sentence))
    
        return max(counts)
