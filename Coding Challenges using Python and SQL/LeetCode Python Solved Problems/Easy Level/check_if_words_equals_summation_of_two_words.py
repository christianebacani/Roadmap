# 1880.) Check if Word Equals Summation of Two Words
# Categories: String

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def getNumericValue(char: str) -> str:
            alphabets = [
                'a', 'b', 'c', 'd',
                'e', 'f', 'g', 'h', 
                'i', 'j'
            ]
            
            for i in range(len(alphabets)):
                if char == alphabets[i]:
                    return str(i)
            
        firstWordNumeric = ''
        secondWordNumeric = ''
        targetWordNumeric = ''
        
        for i in range(len(firstWord)):
            firstWordNumeric += getNumericValue(firstWord[i])

        for i in range(len(secondWord)):
            secondWordNumeric += getNumericValue(secondWord[i])

        for i in range(len(targetWord)):
            targetWordNumeric += getNumericValue(targetWord[i])
        
        if int(firstWordNumeric) + int(secondWordNumeric) == int(targetWordNumeric):
            return True
        
        return False
    