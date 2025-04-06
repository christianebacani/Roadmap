# 1945.) Sum of Digits of String After Convert
# Categories: String, Simulation

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def getAlphabeticalOrder(char: str) -> int:
            alphabets = {
                'a': 1, 'b': '2', 'c': 3, 'd': 4,
                'e': 5, 'f': 6, 'g': 7, 'h': 8,
                'i': 9, 'j': 10, 'k': 11, 'l': 12,
                'm': 13, 'n': 14, 'o': 15, 'p': 16,
                'q': 17, 'r': 18, 's': 19, 't': 20,
                'u': 21, 'v': 22, 'w': 23, 'x': 24,
                'y': 25, 'z': 26
            }
            
            return alphabets[char]

        converted_integers = ''
        
        for i in range(len(s)):
            converted_integers += str(getAlphabeticalOrder(s[i]))
        
        for i in range(k):
            sum = 0
            
            for j in range(len(converted_integers)):
                sum += int(converted_integers[j])
            
            converted_integers = str(sum)
        
        return int(converted_integers)

        
            