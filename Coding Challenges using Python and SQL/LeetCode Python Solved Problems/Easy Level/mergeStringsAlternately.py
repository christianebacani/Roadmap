# 1768.) Merge Strings Alternately
# Categories: Two Pointers, String

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            number_of_elements = len(word1)
        
        elif len(word2) > len(word1):
            number_of_elements = len(word2)
        
        else:
            number_of_elements = len(word1)
        
        result = []

        for i in range(number_of_elements):
            for j in range(len(word1)):
                if i == j:
                    result.append(word1[j])
                    
            for j in range(len(word2)):
                if i == j:
                    result.append(word2[j])
        
        return ''.join(result)