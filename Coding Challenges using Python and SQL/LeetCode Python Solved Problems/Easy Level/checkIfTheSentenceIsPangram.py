# 1832.) Check if the Sentence is Pangram
# Categories: Hash Table, String

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = [
            'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 
            'i',  'j', 'k', 'l', 
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 
            'y', 'z'
        ]
    
        for i in range(len(alphabets)):
            if alphabets[i] not in sentence:
                return False
    
        return True