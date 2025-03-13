# 1662.) Check if Two String Arrays are Equivalent
# Categories: Array, String

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        word1_chars_representation = ''.join(word1)
        word2_chars_representation = ''.join(word2)

        if word1_chars_representation == word2_chars_representation:
            return True
    
        return False
    
