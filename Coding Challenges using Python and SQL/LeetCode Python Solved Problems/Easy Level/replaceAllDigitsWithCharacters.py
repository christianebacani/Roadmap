# 1844.) Replace All Digits with Characters
# Categories: String

class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(char: str, num_of_shift: int) -> str:
            alphabets = [
                'a', 'b', 'c',
                'd', 'e', 'f',
                'g', 'h', 'i',
                'j', 'k', 'l',
                'm', 'n', 'o',
                'p', 'q', 'r',
                's', 't', 'u',
                'v', 'w', 'x',
                'y', 'z'    
            ]
            
            for i in range(len(alphabets)):
                if char == alphabets[i]:
                    return alphabets[i + num_of_shift]
        
        result = ''
        
        for i in range(len(s)):
            if i % 2 != 0:
                result += shift(s[i - 1], int(s[i]))
            
            else:
                result += s[i]
        
        return result